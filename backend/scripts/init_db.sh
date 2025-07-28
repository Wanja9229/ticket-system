#!/bin/bash

echo "🚀 PostgreSQL 데이터베이스 초기화 시작..."

# 사용자가 없으면 생성
sudo -u postgres psql -c "SELECT 1 FROM pg_user WHERE usename = 'ticket_user';" | grep -q 1 || \
sudo -u postgres psql -c "CREATE USER ticket_user WITH PASSWORD '1234';"

# 데이터베이스 삭제 및 재생성
sudo -u postgres psql -c "DROP DATABASE IF EXISTS ticket_system;"
sudo -u postgres psql -c "CREATE DATABASE ticket_system OWNER ticket_user;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ticket_system TO ticket_user;"

echo "✅ 데이터베이스 초기화 완료!"
echo "📌 접속 정보:"
echo "   - Database: ticket_system"
echo "   - User: ticket_user"
echo "   - Password: 1234"
