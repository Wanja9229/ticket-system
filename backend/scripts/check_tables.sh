#!/bin/bash

echo "🔍 ticket_system 데이터베이스 테이블 확인 중..."
echo "================================================"

# 테이블 개수 확인
COUNT=$(sudo -u postgres psql -d ticket_system -t -c "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE';")

echo "📊 총 테이블 수: $COUNT"
echo ""

if [ $COUNT -gt 0 ]; then
    echo "📋 테이블 목록:"
    sudo -u postgres psql -d ticket_system -c "SELECT tablename FROM pg_tables WHERE schemaname = 'public' ORDER BY tablename;"
    
    echo ""
    echo "📐 테이블 상세 정보:"
    sudo -u postgres psql -d ticket_system -c "\dt+"
else
    echo "⚠️  데이터베이스에 테이블이 없습니다."
    echo "   alembic upgrade head 명령을 실행하세요."
fi
