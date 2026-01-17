from abc import ABC, abstractmethod
from typing import List

from rag.models.schemas import DocumentChunk

class BaseChunker(ABC):
    @abstractmethod
    def chunk(self, document: DocumentChunk) -> List[DocumentChunk]:
        raise NotImplementedError