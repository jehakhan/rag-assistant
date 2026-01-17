from typing import List

from rag.chunking.base import BaseChunker
from rag import DocumentChunk

class TokenChunker(BaseChunker):
    def __init__(self, chunk_size: int = 400, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: DocumentChunk) -> List[DocumentChunk]:
        pass

