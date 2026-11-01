
def chunk_pages(pages, chunk_size=100, overlap=20):

    all_chunks = []

    for page in pages:

        words = page["text"].split()

        start = 0

        while start < len(words):

            end = start + chunk_size

            chunk_text = " ".join(words[start:end])

            all_chunks.append({

                "text": chunk_text,

                "metadata": {
                    "source": page["source"],
                    "page_number": page["page_number"]
                }

            })

            start += chunk_size - overlap

    return all_chunks
