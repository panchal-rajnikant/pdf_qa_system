# PDF Question Answering System

This project reads text from a PDF, splits the extracted text into overlapping
chunks, and prints a short preview of the results with page and source metadata.

## Requirements

- Python
- PyMuPDF

Install the dependency from the project root:

```powershell
python -m pip install -r requirements.txt
```

## Add a PDF

Place the PDF at `data/sample.pdf`. The input path is resolved relative to
`src/main.py`, so it does not depend on the directory from which you run the
script.

## Run

From the project root:

```powershell
python src\main.py
```

The script prints the number of pages read, the number of chunks created, and
the first three chunks with their metadata.

## How PDF reading and chunking work

1. `src/ingestion/pdf_loader.py` opens the PDF with PyMuPDF and extracts text
   page by page.
2. Each page is represented by its extracted text, a one-based page number,
   and the PDF source path.
3. `src/ingestion/chunker.py` splits each page's text on whitespace and groups
   the words into chunks of 100 words, with a 20-word overlap between chunks.
4. Each chunk contains its text and metadata (`source` and `page_number`).

The chunk size and overlap can be changed through the `chunk_size` and
`overlap` arguments to `chunk_pages(pages, chunk_size=100, overlap=20)`.