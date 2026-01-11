from typing import List
import re

from rag.loaders.base import BaseLoader
from rag import DocumentChunk


class MarkdownLoader(BaseLoader):
    def load(self) -> List[DocumentChunk]:
        text = self.source_path.read_text(encoding="utf-8")

        text = re.sub(r"\n{3,}", "\n\n", text).strip()

        return [
            DocumentChunk(
                chunk_id=self.source_path.stem,
                text=text,
                source=str(self.source_path),
                section=None,
            )
        ]