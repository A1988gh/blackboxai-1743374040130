from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import Config

# تنظیمات اتصال به دیتابیس
engine = create_engine(
    Config.DATABASE_URI,
    connect_args={"check_same_thread": False}  # فقط برای SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    """تابع ایجاد جداول دیتابیس"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """
    تابع تهیه session دیتابیس برای FastAPI
    الگوی Dependency Injection
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()