-- ticket_system 데이터베이스에 연결한 상태에서 실행

-- 기존 테이블들에 대한 모든 권한 부여
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ticket_user;

-- 시퀀스에 대한 권한 부여 (SERIAL 컬럼 때문에 필요)
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ticket_user;

-- 함수에 대한 권한 부여
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO ticket_user;

-- 앞으로 생성될 테이블에 대한 기본 권한 설정
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO ticket_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO ticket_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO ticket_user;

-- 스키마 사용 권한 확인/부여
GRANT USAGE ON SCHEMA public TO ticket_user;

-- 권한 확인
SELECT 
    table_name,
    privilege_type
FROM information_schema.table_privileges 
WHERE grantee = 'ticket_user' 
ORDER BY table_name, privilege_type;