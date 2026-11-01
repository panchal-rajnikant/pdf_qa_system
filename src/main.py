from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_pages
from pathlib import Path

def main():

    
    pdf_path = Path(__file__).resolve().parent.parent / "data" / "sample.pdf"
    pages = load_pdf(str(pdf_path))
    print("Total pages:", len(pages))

    chunks = chunk_pages(pages)

    print("Total chunks:", len(chunks))

    for chunk in chunks[:3]:

        print("\nChunk:")
        print(chunk["text"])

        print("Metadata:")
        print(chunk["metadata"])


if __name__ == "__main__":
    main()