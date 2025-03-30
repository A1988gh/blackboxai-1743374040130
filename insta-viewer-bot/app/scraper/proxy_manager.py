import random
import logging
from typing import List, Optional
from ..config import Config

logger = logging.getLogger(__name__)

class ProxyManager:
    """مدیریت چرخش و سلامت پروکسی‌ها"""
    
    def __init__(self):
        self.proxies: List[str] = Config.PROXY_LIST
        self.current_proxy: Optional[str] = None
        self.blacklist: List[str] = []
        
    def get_random_proxy(self) -> Optional[str]:
        """دریافت یک پروکسی تصادفی از لیست"""
        if not self.proxies:
            logger.warning("لیست پروکسی‌ها خالی است")
            return None
            
        available_proxies = [p for p in self.proxies if p not in self.blacklist]
        if not available_proxies:
            logger.warning("هیچ پروکسی در دسترس نیست")
            return None
            
        self.current_proxy = random.choice(available_proxies)
        return self.current_proxy
        
    def mark_proxy_failed(self, proxy: str):
        """علامت گذاری پروکسی ناموفق"""
        if proxy not in self.blacklist:
            self.blacklist.append(proxy)
            logger.warning(f"پروکسی {proxy} به لیست سیاه اضافه شد")
            
    def clear_blacklist(self):
        """پاک کردن لیست سیاه پروکسی‌ها"""
        self.blacklist.clear()
        logger.info("لیست سیاه پروکسی‌ها پاک شد")
        
    def health_check(self, proxy: str) -> bool:
        """بررسی سلامت پروکسی"""
        # TODO: پیاده‌سازی بررسی واقعی
        return True
        
    def get_current_proxy(self) -> Optional[str]:
        """دریافت پروکسی فعلی"""
        return self.current_proxy