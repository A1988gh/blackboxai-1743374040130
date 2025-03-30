from fastapi import FastAPI
from telegram.ext import Application
from .config import Config

# Initialize FastAPI app for admin panel
web_app = FastAPI(
    title="پنل مدیریت ربات اینستاگرام ویور",
    description="سیستم مدیریت ربات مشاهده پست و استوری اینستاگرام",
    version="1.0.0"
)

# Initialize Telegram bot
telegram_bot = Application.builder() \
    .token(Config.TELEGRAM_TOKEN) \
    .build()

def setup_app():
    """تنظیمات اولیه برنامه"""
    
    # Import and register handlers
    from .bot import handlers_fa
    from .admin import views
    
    # ثبت هندلرهای فارسی
    telegram_bot.add_handler(handlers_fa.start_handler)
    telegram_bot.add_handler(handlers_fa.help_handler) 
    telegram_bot.add_handler(handlers_fa.username_handler)
    
    # تنظیمات دیتابیس
    from .models import init_db
    init_db()
    
    # تنظیمات لاگینگ
    import logging
    logging.basicConfig(
        level=Config.LOG_LEVEL,
        filename=Config.LOG_FILE,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )

# اجرای تنظیمات هنگام ایمپورت
setup_app()