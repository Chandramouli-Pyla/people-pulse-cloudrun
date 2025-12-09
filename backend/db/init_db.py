from .connection import Base, engine
from backend.core.logging_config import logger  # import logger

# Import other models here as you create them

def init_db():
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Tables created successfully.")
    except Exception as e:
        logger.exception(f"Error while creating tables: {e}")

if __name__ == "__main__":
    init_db()
