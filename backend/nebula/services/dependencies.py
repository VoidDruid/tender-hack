from typing import Generator

from pymongo import MongoClient

from conf import DB_URI, db_settings


# FastAPI Dependency
def get_db():
    db = None
    try:
        print(DB_URI)
        client = MongoClient(DB_URI)
        db = client[db_settings.DATABASE_NAME]
        yield db[' clients']
    finally:
        if client:
            client.close()
