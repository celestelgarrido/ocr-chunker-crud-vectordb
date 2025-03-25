

from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker

def chunking_text():

    DOC_SOURCE = "./app/files/output/docling-paper.md"
    print(DOC_SOURCE)

    doc = DocumentConverter().convert(source=DOC_SOURCE).document

    print(doc)

    chunker = HybridChunker()
    chunk_iter = chunker.chunk(dl_doc=doc)

    print(enumerate(chunk_iter))
    for i, chunk in enumerate(chunk_iter):
        print(f"=== {i} ===")
        print(f"chunk.text:\n{repr(f'{chunk.text[:300]}…')}")

        enriched_text = chunker.serialize(chunk=chunk)
        print(f"chunker.serialize(chunk):\n{repr(f'{enriched_text[:300]}…')}")

        print()