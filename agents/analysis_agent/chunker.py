from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str):
    """
    Split large paper text into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=300,
        separators=["\n\n", "\n", ".", " "]
    )

    return splitter.split_text(text)