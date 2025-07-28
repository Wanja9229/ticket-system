import qrcode
from io import BytesIO
import base64
from typing import Optional


def generate_qr_code(data: str, size: int = 10, border: int = 1) -> str:
    """QR 코드 생성 (base64 인코딩된 이미지 반환)"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    
    return f"data:image/png;base64,{img_str}"


def generate_ticket_qr(ticket_number: str, order_id: str) -> str:
    """티켓 QR 코드 생성"""
    data = f"TICKET:{ticket_number}|ORDER:{order_id}"
    return generate_qr_code(data)
