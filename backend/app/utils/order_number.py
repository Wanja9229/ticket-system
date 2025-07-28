import random
import string
from datetime import datetime
from typing import Optional


def generate_order_number(prefix: str = "ORD") -> str:
    """주문번호 생성 (ORD20250728123456789)"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}{timestamp}{random_suffix}"


def generate_ticket_number(event_code: str, index: int) -> str:
    """티켓번호 생성 (AAA-20250728-00001)"""
    date_str = datetime.now().strftime("%Y%m%d")
    return f"{event_code.upper()}-{date_str}-{index:05d}"


def validate_order_number(order_number: str) -> bool:
    """주문번호 유효성 검증"""
    if not order_number or len(order_number) < 20:
        return False
    
    # Check prefix
    if not order_number.startswith("ORD"):
        return False
    
    # Check if the rest are digits
    if not order_number[3:].isdigit():
        return False
    
    return True
