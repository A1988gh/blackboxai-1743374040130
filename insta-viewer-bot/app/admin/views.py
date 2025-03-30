from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.request import RequestModel
from app.database import get_db

router = APIRouter()

@router.get("/admin/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request, db: Session = Depends(get_db)):
    # آمار کاربران
    user_count = db.query(User).count()
    active_users = db.query(User).filter(User.is_active == True).count()
    
    # آمار درخواست‌ها
    total_requests = db.query(RequestModel).count()
    completed_requests = db.query(RequestModel).filter(RequestModel.status == 'completed').count()
    
    return {
        "user_count": user_count,
        "active_users": active_users,
        "total_requests": total_requests,
        "completed_requests": completed_requests
    }

@router.get("/admin/users", response_class=HTMLResponse)
async def admin_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).order_by(User.created_at.desc()).limit(50).all()
    return {"users": users}