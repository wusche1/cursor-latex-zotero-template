#!/usr/bin/env python3
"""Add an arXiv paper to Zotero with PDF attachment."""

import sys
import os
import re
import json
import urllib.request
from pathlib import Path
from xml.etree import ElementTree

API_KEY = os.environ.get("ZOTERO_API_KEY")
if not API_KEY:
    print("Error: ZOTERO_API_KEY not set")
    sys.exit(1)

USER_ID = None


def get_user_id():
    global USER_ID
    if USER_ID:
        return USER_ID
    req = urllib.request.Request(
        f"https://api.zotero.org/keys/{API_KEY}",
        headers={"Zotero-API-Key": API_KEY}
    )
    USER_ID = json.loads(urllib.request.urlopen(req).read())["userID"]
    return USER_ID


def api_request(endpoint, method="GET", data=None, headers=None):
    user_id = get_user_id()
    url = f"https://api.zotero.org/users/{user_id}/{endpoint}"
    hdrs = {"Zotero-API-Key": API_KEY, "Content-Type": "application/json"}
    if headers:
        hdrs.update(headers)

    if data is not None:
        req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=hdrs, method=method)
    else:
        req = urllib.request.Request(url, headers=hdrs, method=method)

    resp = urllib.request.urlopen(req)
    body = resp.read()
    return json.loads(body) if body else None


def get_collection_key(name_or_key):
    collections = api_request("collections")
    for c in collections:
        if c["data"]["key"] == name_or_key or c["data"]["name"].lower() == name_or_key.lower():
            return c["data"]["key"]
    return None


def parse_arxiv(url_or_id):
    match = re.search(r"(\d{4}\.\d{4,5})", url_or_id)
    if not match:
        return None, None

    arxiv_id = match.group(1)

    try:
        metadata = parse_arxiv_api(arxiv_id)
    except Exception as e:
        print(f"API failed ({e}), trying HTML fallback...")
        metadata = parse_arxiv_html(arxiv_id)

    return arxiv_id, metadata


def parse_arxiv_api(arxiv_id):
    api_url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
    req = urllib.request.Request(api_url, headers={"User-Agent": "ZoteroSkill/1.0"})
    xml = urllib.request.urlopen(req, timeout=10).read().decode()

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ElementTree.fromstring(xml)
    entry = root.find("atom:entry", ns)
    if entry is None:
        raise Exception("No entry found")

    title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
    abstract = entry.find("atom:summary", ns).text.strip()
    published = entry.find("atom:published", ns).text[:10]

    authors = []
    for author in entry.findall("atom:author", ns):
        name = author.find("atom:name", ns).text
        parts = name.rsplit(" ", 1)
        if len(parts) == 2:
            authors.append({"creatorType": "author", "firstName": parts[0], "lastName": parts[1]})
        else:
            authors.append({"creatorType": "author", "name": name})

    return {
        "itemType": "preprint",
        "title": title,
        "abstractNote": abstract,
        "creators": authors,
        "date": published,
        "url": f"https://arxiv.org/abs/{arxiv_id}",
        "repository": "arXiv",
        "archiveID": f"arXiv:{arxiv_id}",
    }


def parse_arxiv_html(arxiv_id):
    url = f"https://arxiv.org/abs/{arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    html = urllib.request.urlopen(req, timeout=10).read().decode()

    title_match = re.search(r'<meta name="citation_title" content="([^"]+)"', html)
    title = title_match.group(1) if title_match else "Unknown"

    authors = []
    for m in re.finditer(r'<meta name="citation_author" content="([^"]+)"', html):
        name = m.group(1)
        parts = name.rsplit(", ", 1)
        if len(parts) == 2:
            authors.append({"creatorType": "author", "firstName": parts[1], "lastName": parts[0]})
        else:
            authors.append({"creatorType": "author", "name": name})

    date_match = re.search(r'<meta name="citation_date" content="([^"]+)"', html)
    date = date_match.group(1) if date_match else ""

    abstract_match = re.search(r'<meta name="citation_abstract" content="([^"]+)"', html, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else ""

    return {
        "itemType": "preprint",
        "title": title,
        "abstractNote": abstract,
        "creators": authors,
        "date": date,
        "url": url,
        "repository": "arXiv",
        "archiveID": f"arXiv:{arxiv_id}",
    }


def download_pdf(arxiv_id):
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"Downloading PDF from {pdf_url}...")
    req = urllib.request.Request(pdf_url, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    content = urllib.request.urlopen(req, timeout=60).read()
    filename = f"{arxiv_id.replace('.', '_')}.pdf"
    return content, filename


def save_attachment_local(parent_key, pdf_content, filename):
    attachment = {
        "itemType": "attachment",
        "parentItem": parent_key,
        "linkMode": "imported_file",
        "title": filename,
        "contentType": "application/pdf",
        "filename": filename,
    }

    result = api_request("items", method="POST", data=[attachment])
    if not result.get("successful"):
        print(f"Failed to create attachment: {result}")
        return False

    attach_key = list(result["successful"].values())[0]["key"]
    print(f"Created attachment item: {attach_key}")

    zotero_storage = Path.home() / "Zotero" / "storage" / attach_key
    zotero_storage.mkdir(parents=True, exist_ok=True)

    pdf_path = zotero_storage / filename
    pdf_path.write_bytes(pdf_content)
    print(f"Saved PDF to: {pdf_path}")

    return True


def create_item(metadata, collection_key=None):
    if collection_key:
        metadata["collections"] = [collection_key]

    result = api_request("items", method="POST", data=[metadata])
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: add-paper.py <arxiv-url-or-id> [collection-name]")
        sys.exit(1)

    url_or_id = sys.argv[1]
    collection = sys.argv[2] if len(sys.argv) > 2 else None

    collection_key = None
    if collection:
        collection_key = get_collection_key(collection)
        if not collection_key:
            print(f"Error: Collection '{collection}' not found")
            sys.exit(1)

    arxiv_id, metadata = parse_arxiv(url_or_id)
    if not metadata:
        print("Error: Could not parse arXiv ID from input")
        sys.exit(1)

    print(f"Title: {metadata['title']}")
    print(f"Authors: {', '.join(c.get('lastName', c.get('name')) for c in metadata['creators'])}")

    result = create_item(metadata, collection_key)
    if not result.get("successful"):
        print(f"Error creating item: {result}")
        sys.exit(1)

    parent_key = list(result["successful"].values())[0]["key"]
    print(f"Created item: {parent_key}")

    try:
        pdf_content, filename = download_pdf(arxiv_id)
        save_attachment_local(parent_key, pdf_content, filename)
    except Exception as e:
        print(f"Warning: Could not attach PDF: {e}")

    print("Done!")
