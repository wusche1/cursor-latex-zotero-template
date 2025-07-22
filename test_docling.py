from docling.document_converter import DocumentConverter
import os

def test_docling():
    source = "bib/turner2023/turner2023.pdf"  # Use the long PDF
    if not os.path.exists(source):
        print(f"PDF file not found: {source}")
        return
    
    converter = DocumentConverter()
    result = converter.convert(source)
    markdown_content = result.document.export_to_markdown()
    print(f"Extracted {len(markdown_content)} characters")
    print("First 500 characters:")
    print(markdown_content[:500])
    with open("extracted_content.md", "w") as f:
        f.write(markdown_content)
    print("Full content saved to extracted_content.md")

if __name__ == "__main__":
    test_docling() 