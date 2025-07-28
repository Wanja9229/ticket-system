"""
데이터베이스 뷰 모델
"""

from sqlalchemy import Table, Column, String, Text, BigInteger, Numeric

from .base import Base


# PostgreSQL 연결 통계 뷰
t_v_connection_stats = Table(
    'v_connection_stats', Base.metadata,
    Column('database_name', String),
    Column('state', Text),
    Column('connection_count', BigInteger),
    Column('max_query_duration_seconds', Numeric)
)
