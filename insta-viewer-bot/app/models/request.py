from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class RequestModel(Base):
    """مدل جامع برای پیگیری درخواست‌های کاربران"""
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    instagram_username = Column(String(50), nullable=False)
    request_type = Column(String(20), nullable=False)  # story/post/highlight/profile
    request_data = Column(JSON)  # ذخیره پارامترهای اضافی
    status = Column(String(20), default='pending')  # pending/processing/completed/failed
    result_count = Column(Integer)  # تعداد محتواهای دریافت شده
    media_urls = Column(JSON)  # لیست URLهای دریافت شده
    error_details = Column(String(500))  # جزئیات خطا در صورت وجود
    ip_address = Column(String(50))  # آی‌پی کاربر
    user_agent = Column(String(300))  # اطلاعات مرورگر کاربر
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))

    # رابطه با مدل User
    user = relationship("User", back_populates="requests")

    def __repr__(self):
        return f"<RequestModel(id={self.id}, type={self.request_type}, status={self.status})>"

    def get_duration(self):
        """محاسبه مدت زمان پردازش درخواست"""
        if self.started_at and self.completed_at:
            return (self.completed_at - self.started_at).total_seconds()
        return None