from fastapi import APIRouter, Depends

from ..auth.base_config import current_user

from .tasks import send_email_report, calculate_pdf

router = APIRouter(prefix="/report",
                   tags=["all slow functions"])


@router.get("/email_ready")
def get_report(user=Depends(current_user)):
    send_email_report.delay(user.username, user.email)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }

@router.get('/make_a_report')
def make_report(user=Depends(current_user)):
    calculate_pdf.delay(user.username, user.email, user.id)