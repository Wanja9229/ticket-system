from datetime import datetime, date, timedelta
from typing import Optional


def get_korea_time() -> datetime:
    """한국 시간 가져오기"""
    # UTC+9
    return datetime.utcnow() + timedelta(hours=9)


def format_datetime(dt: datetime, format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """날짜시간 포맷팅"""
    return dt.strftime(format)


def parse_date(date_str: str) -> Optional[date]:
    """문자열을 날짜로 파싱"""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def get_date_range(start_date: date, end_date: date) -> list[date]:
    """두 날짜 사이의 모든 날짜 리스트 반환"""
    delta = end_date - start_date
    return [start_date + timedelta(days=i) for i in range(delta.days + 1)]
