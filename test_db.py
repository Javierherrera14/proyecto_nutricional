from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

print("DATABASE_URL raw:", repr(database_url))

try:
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    db.execute(text("SELECT 1"))  # ✅ corrección aquí
    print("Conexión exitosa a la base de datos.")
except Exception as e:
    print("Error al conectar:", repr(e))
