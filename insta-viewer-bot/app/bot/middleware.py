from telegram import Update
from telegram.ext import ContextTypes
from ..config import Config
import logging

logger = logging.getLogger(__name__)

async def auth_middleware(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """میدلور احراز هویت کاربران"""
    user = update.effective_user
    if not user:
        logger.warning("درخواست بدون کاربر دریافت شد")
        return False
        
    logger.info(f"درخواست از کاربر: {user.id} - {user.username}")
    return True

async def rate_limit_middleware(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """میدلور محدودیت نرخ درخواست"""
    user_id = update.effective_user.id
    # TODO: پیاده‌سازی منطق محدودیت درخواست
    return True

async def language_middleware(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """تنظیم زبان پیش‌فرض به فارسی"""
    context.user_data['lang'] = 'fa'
    return True