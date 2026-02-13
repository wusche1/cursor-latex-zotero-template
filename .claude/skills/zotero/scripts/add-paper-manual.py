#!/usr/bin/env python3
"""Add a paper to Zotero with manually provided metadata and PDF URL."""

import sys
import os
import json
import argparse
import urllib.request
from pathlib import Path

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


def parse_authors(authors_str):
    creators = []
    for author in authors_str.split(","):
        author = author.strip()
        if not author:
            continue
        parts = author.rsplit(" ", 1)
        if len(parts) == 2:
            creators.append({"creatorType": "author", "firstName": parts[0], "lastName": parts[1]})
        else:
            creators.append({"creatorType": "author", "name": author})
    return creators


def download_pdf(url):
    print(f"Downloading PDF from {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    return urllib.request.urlopen(req, timeout=120).read()


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
    return api_request("items", method="POST", data=[metadata])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a paper to Zotero with manual metadata")
    parser.add_argument("--pdf", required=True, help="URL to the PDF file")
    parser.add_argument("--title", required=True, help="Paper title")
    parser.add_argument("--authors", required=True, help="Comma-separated author names (e.g., 'John Smith, Jane Doe')")
    parser.add_argument("--year", required=True, help="Publication year")
    parser.add_argument("--url", help="URL to the paper page (not the PDF)")
    parser.add_argument("--abstract", help="Paper abstract")
    parser.add_argument("--type", default="report", choices=["report", "preprint", "journalArticle", "conferencePaper", "webpage"], help="Item type")
    parser.add_argument("--publisher", help="Publisher or institution name")
    parser.add_argument("--collection", help="Zotero collection name or key")

    args = parser.parse_args()

    collection_key = None
    if args.collection:
        collection_key = get_collection_key(args.collection)
        if not collection_key:
            print(f"Error: Collection '{args.collection}' not found")
            sys.exit(1)

    metadata = {
        "itemType": args.type,
        "title": args.title,
        "creators": parse_authors(args.authors),
        "date": args.year,
    }

    if args.url:
        metadata["url"] = args.url
    if args.abstract:
        metadata["abstractNote"] = args.abstract
    if args.publisher:
        if args.type == "report":
            metadata["institution"] = args.publisher
        else:
            metadata["publisher"] = args.publisher

    print(f"Title: {metadata['title']}")
    print(f"Authors: {', '.join(c.get('lastName', c.get('name')) for c in metadata['creators'])}")
    print(f"Year: {args.year}")

    result = create_item(metadata, collection_key)
    if not result.get("successful"):
        print(f"Error creating item: {result}")
        sys.exit(1)

    parent_key = list(result["successful"].values())[0]["key"]
    print(f"Created item: {parent_key}")

    try:
        pdf_content = download_pdf(args.pdf)
        filename = args.pdf.split("/")[-1]
        if not filename.endswith(".pdf"):
            filename = f"{args.title[:50].replace(' ', '_')}.pdf"
        save_attachment_local(parent_key, pdf_content, filename)
    except Exception as e:
        print(f"Warning: Could not attach PDF: {e}")

    print("Done!")
