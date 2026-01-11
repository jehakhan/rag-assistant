from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from rag.models.schemas import DocumentChunk


class BaseLoader(ABC):
    def __init__(self, source_path: Path):
        self.source_path = source_path

    @abstractmethod
    def load(self) -> List[DocumentChunk]:
        """Load documents and return normalized text chunks (1 per document)."""
        raise NotImplementedError