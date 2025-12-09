from backend.db.connection import get_db

# This is just to import get_db as a FastAPI dependency
db_dependency = get_db
