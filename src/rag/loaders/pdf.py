from typing import List

from pypdf import PdfReader

from rag.loaders.base import BaseLoader
from rag import DocumentChunk


class PDFLoader(BaseLoader):
    def load(self) -> List[DocumentChunk]:
        reader = PdfReader(str(self.source_path))
        pages = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text.strip())

        full_text = "\n\n".join(pages)

        return [
            DocumentChunk(
                chunk_id=self.source_path.stem,
                text=full_text,
                source=str(self.source_path),
                section=None,
            )]
