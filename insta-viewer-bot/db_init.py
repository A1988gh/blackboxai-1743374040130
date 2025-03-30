from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.config import Config

# Create isolated database configuration
Base = declarative_base()
engine = create_engine(Config.DATABASE_URI, connect_args={"check_same_thread": False})

# Import models directly (avoid app imports)
from app.models.base import Base as ModelsBase
from app.models.user import User
from app.models.request import RequestModel

def initialize_database():
    print("Creating database tables...")
    ModelsBase.metadata.create_all(bind=engine)
    print("All tables created successfully!")

if __name__ == "__main__":
    initialize_database()