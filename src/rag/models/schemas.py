from typing import Optional
from pydantic import BaseModel


class DocumentChunk(BaseModel):
    """
    Immutable data structure representing a unit of text
    flowing through the RAG pipeline.

    At different stages:
    - loader   → whole document
    - chunker  → partial document
    - retriever→ retrieved chunk
    """

    chunk_id: str
    text: str
    source: str
    section: Optional[str] = None
