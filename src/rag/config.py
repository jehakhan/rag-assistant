from pathlib import Path
from dotenv import  load_dotenv
from common import get_logger
import os

load_dotenv()
logger = get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parents[2]
logger.info(BASE_DIR)
DATA_DIR = BASE_DIR / "data"
logger.info(DATA_DIR)
RAW_DATA_DIR = DATA_DIR / "raw"
logger.info(RAW_DATA_DIR)
PROCESSED_DATA_DIR = DATA_DIR / "processed"
logger.info(PROCESSED_DATA_DIR)
VECTOR_DB_DIR = DATA_DIR / "chroma"
logger.info(VECTOR_DB_DIR)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2",
)

LLM_MODEL = os.getenv("LLM_MODEL", "phi3:mini")
