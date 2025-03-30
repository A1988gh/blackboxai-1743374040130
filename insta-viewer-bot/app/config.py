import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Telegram Bot Token
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '8189453320:AAF6MvOOSE4JDiN7De8Uy-RNZI1CroDj2ng')
    
    # Instagram API Credentials
    INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
    INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
    
    # Database Configuration
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///insta_viewer.db')
    
    # Proxy Settings
    PROXY_ENABLED = os.getenv('PROXY_ENABLED', 'False') == 'True'
    PROXY_LIST = os.getenv('PROXY_LIST', '').split(',') if os.getenv('PROXY_LIST') else []
    PROXY_TIMEOUT = int(os.getenv('PROXY_TIMEOUT', '30'))  # ثانیه
    PROXY_MAX_RETRY = int(os.getenv('PROXY_MAX_RETRY', '3'))
    
    # Instagram API Settings
    USER_AGENT = os.getenv('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    INSTAGRAM_APP = {
        'app_version': '10.0.0',
        'android_version': '29',
        'android_release': '10',
        'dpi': '480dpi',
        'resolution': '1080x1920',
        'manufacturer': 'Xiaomi',
        'device': 'Mi 9T',
        'cpu': 'qcom',
        'version_code': '10000000'
    }
    
    # Rate Limiting
    USER_RATE_LIMIT = int(os.getenv('USER_RATE_LIMIT', '5'))  # requests per hour
    FREE_TRIAL_LIMIT = int(os.getenv('FREE_TRIAL_LIMIT', '3'))  # free requests
    
    # Admin Panel
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'insta_viewer.log')