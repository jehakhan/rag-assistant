from pathlib import Path

from rag.loaders.markdown import MarkdownLoader
from rag.loaders.pdf import PDFLoader

def get_loader(path: Path):
    if path.suffix.lower() in {".md", ".markdown"}:
        return MarkdownLoader(path)
    if path.suffix.lower() == ".pdf":
        return PDFLoader(path)
    raise ValueError(f"Unsupported file type: {path.suffix}")