
CREATE TABLE IF NOT EXISTS todos (
    -- Primary Key
    id SERIAL PRIMARY KEY,
    
    -- Todo 기본 필드
    title VARCHAR(200) NOT NULL,
    description TEXT,
    priority VARCHAR(10) NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high')),
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed')),
    due_date TIMESTAMP,
    
    -- 완료 관련 필드
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    completed_at TIMESTAMP,
    
    -- 감사(Audit) 필드
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    -- Soft Delete 필드
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
    deleted_at TIMESTAMP
);
-- 테이블 코멘트 추가
COMMENT ON TABLE todos IS 'Todo 항목 관리 테이블';
COMMENT ON COLUMN todos.id IS 'Todo ID (Primary Key)';
COMMENT ON COLUMN todos.title IS '할 일 제목';
COMMENT ON COLUMN todos.description IS '상세 설명';
COMMENT ON COLUMN todos.priority IS '우선순위: low, medium, high';
COMMENT ON COLUMN todos.status IS '진행 상태: pending, in_progress, completed';
COMMENT ON COLUMN todos.due_date IS '마감일시';
COMMENT ON COLUMN todos.is_completed IS '완료 여부';
COMMENT ON COLUMN todos.completed_at IS '완료 시간';
COMMENT ON COLUMN todos.created_by IS '생성자 사용자 ID';
COMMENT ON COLUMN todos.created_at IS '생성 시간';
COMMENT ON COLUMN todos.updated_at IS '마지막 수정 시간';
COMMENT ON COLUMN todos.is_deleted IS '삭제 여부 (Soft Delete)';
COMMENT ON COLUMN todos.deleted_at IS '삭제 시간';


INSERT INTO todos (title, description, priority, status, due_date, created_by) 
VALUES 
    ('프로젝트 기획서 작성', '다음 주 발표용 기획서 초안 작성', 'high', 'in_progress', '2024-12-25 18:00:00', 1),
    ('코드 리뷰', '팀원들 PR 리뷰하기', 'medium', 'pending', '2024-12-23 12:00:00', 1),
    ('회의 준비', '주간 회의 자료 준비', 'low', 'completed', '2024-12-22 10:00:00', 1);
















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

admin1234 암호화된 비밀번호
$2b$12$1Lu3u0TD8Iva58SXREqDmOtSp/6fYaM.7i7xh0zbWg99vqacxPT6i
