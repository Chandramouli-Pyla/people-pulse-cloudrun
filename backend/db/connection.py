from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
from backend.core.logging_config import logger

load_dotenv()

BQ_PROJECT_ID = os.getenv("BIGQUERY_PROJECT_ID")
BQ_DATASET = os.getenv("BIGQUERY_DATASET")

DATABASE_URL = f"bigquery://{BQ_PROJECT_ID}/{BQ_DATASET}"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger.info(f"Connected to BigQuery dataset: {BQ_PROJECT_ID}.{BQ_DATASET}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

################POSTGRESQL STEUP###########################################

# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# import os
# from dotenv import load_dotenv
# from backend.app.core.logging_config import logger  # import logger
#
# # Load environment variables
# load_dotenv()
#
# DB_USER = os.getenv("POSTGRES_USER", "postgres")
# DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
# DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
# DB_PORT = os.getenv("POSTGRES_PORT", "5432")
# DB_NAME = os.getenv("POSTGRES_DB", "peoplepulse_db")
#
# DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#
# # Create the SQLAlchemy engine and log SQL statements
# engine = create_engine(DATABASE_URL, echo=True, future=True)
#
# logger.info(f"Connected to database: {DB_NAME} at {DB_HOST}:{DB_PORT}")
#
# # Base class
# Base = declarative_base()
#
# # Session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
