from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunking_text():

    with open("./app/files/output/docling-paper.md", 'r', encoding='utf-8') as file:
        text = file.read()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20, separators=["\n\n"])
    chunks = text_splitter.split_text(text)
    
    # Prints chunks with a line separator
    #for chunk in chunks:
    #    print(chunk)
    #    print("-" * 40)

    return chunks


def semantic_chunking_text():
    print("")

