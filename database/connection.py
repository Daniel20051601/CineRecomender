import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_engine():
    try:
        engine = create_engine(os.getenv("DATABASE_URL"))
        return engine
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None
        