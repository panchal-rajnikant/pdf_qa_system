import pymupdf

def load_pdf(file_path):

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document):

        text = page.get_text()

        pages.append({
            "text": text,
            "page_number": page_number + 1,
            "source": file_path
        })

    document.close()

    return pages