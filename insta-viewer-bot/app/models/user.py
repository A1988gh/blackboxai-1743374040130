from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    """مدل کاربران سیستم با قابلیت‌های مدیریتی"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String(50), unique=True, index=True, nullable=False)
    username = Column(String(50), index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone_number = Column(String(15))
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    subscription_type = Column(String(20), default='free')
    remaining_requests = Column(Integer, default=3)
    last_request_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship with RequestModel
    requests = relationship("RequestModel", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username=@{self.username})>"

    def get_full_name(self):
        """دریافت نام کامل کاربر"""
        return f"{self.first_name} {self.last_name}".strip()