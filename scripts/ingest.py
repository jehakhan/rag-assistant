from pathlib import Path
from rag.pipeline.ingest import ingest_directory
from rag.config import RAW_DATA_DIR

from common import get_logger

logger = get_logger(__name__)

docs = ingest_directory(RAW_DATA_DIR)
logger.info(f"Ingested {len(docs)} documents")
