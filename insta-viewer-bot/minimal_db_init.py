from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Minimal database configuration
DATABASE_URI = "sqlite:///./test.db"  # Using a new database file
Base = declarative_base()
engine = create_engine(DATABASE_URI, connect_args={"check_same_thread": False})

# Define minimal versions of the models we need
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String(50), unique=True, index=True)
    username = Column(String(50))
    is_active = Column(Integer)

class RequestModel(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    status = Column(String(20))

def initialize_database():
    print("Creating database tables with minimal configuration...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully in test.db!")

if __name__ == "__main__":
    initialize_database()