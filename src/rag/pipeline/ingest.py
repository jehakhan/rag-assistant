from pathlib import Path
from typing import List

from rag.loaders import get_loader
from rag.models.schemas import DocumentChunk
from common import get_logger

logger = get_logger(__name__)


def ingest_directory(path: Path) -> List[DocumentChunk]:
    documents: List[DocumentChunk] = []

    for file in path.rglob("*"):
        if file.is_file():
            try:
                loader = get_loader(file)
                docs = loader.load()
                documents.extend(docs)
                logger.info(f"Loaded {file}")
            except ValueError:
                continue
    return documents
