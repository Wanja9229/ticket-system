"""
Week 2 - Day 3 과제

간단한 게시판 API 만들기
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="게시판 API")

# 과제 1: 게시글 모델 정의
class PostBase(BaseModel):
    """
    게시글 기본 모델
    필드:
    - title: 제목 (필수, 최대 100자)
    - content: 내용 (필수)
    - author: 작성자 (필수)
    - category: 카테고리 (선택, 기본값 "general")
    """
    # TODO: 구현하세요
    pass


class PostCreate(PostBase):
    """게시글 생성 요청"""
    # TODO: 구현하세요
    pass


class PostUpdate(BaseModel):
    """
    게시글 수정 요청
    모든 필드는 선택적
    """
    # TODO: 구현하세요
    pass


class PostResponse(PostBase):
    """
    게시글 응답
    추가 필드:
    - id: 게시글 ID
    - created_at: 생성일시
    - updated_at: 수정일시
    - views: 조회수
    """
    # TODO: 구현하세요
    pass


# 과제 2: 가짜 데이터베이스 구현
posts_db = {}
post_counter = 0


# 과제 3: API 엔드포인트 구현

@app.post("/posts/", response_model=PostResponse)
def create_post(post: PostCreate):
    """
    새 게시글 작성
    - ID는 자동 생성
    - created_at은 현재 시간
    - views는 0으로 시작
    """
    # TODO: 구현하세요
    pass


@app.get("/posts/", response_model=List[PostResponse])
def get_posts(
    category: Optional[str] = None,
    skip: int = 0,
    limit: int = 10
):
    """
    게시글 목록 조회
    - category로 필터링 가능
    - 페이지네이션 지원
    """
    # TODO: 구현하세요
    pass


@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    """
    특정 게시글 조회
    - 조회 시 views +1 증가
    - 없는 ID면 404 에러
    """
    # TODO: 구현하세요
    pass


@app.put("/posts/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post_update: PostUpdate):
    """
    게시글 수정
    - updated_at 갱신
    - 없는 ID면 404 에러
    """
    # TODO: 구현하세요
    pass


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    """
    게시글 삭제
    - 성공 시 {"message": "Post deleted"} 반환
    - 없는 ID면 404 에러
    """
    # TODO: 구현하세요
    pass


# 과제 4: 추가 기능 구현

@app.get("/posts/search/")
def search_posts(q: str):
    """
    게시글 검색
    - 제목이나 내용에 검색어(q)가 포함된 게시글 반환
    - 대소문자 구분 없이 검색
    """
    # TODO: 구현하세요
    pass


@app.get("/posts/top/")
def get_top_posts(limit: int = 5):
    """
    인기 게시글 조회
    - 조회수(views) 기준 상위 N개 반환
    """
    # TODO: 구현하세요
    pass


# 과제 5: 댓글 기능 추가 (보너스)
class CommentCreate(BaseModel):
    """댓글 생성"""
    # TODO: 구현하세요
    pass


class CommentResponse(BaseModel):
    """댓글 응답"""
    # TODO: 구현하세요
    pass


@app.post("/posts/{post_id}/comments/")
def create_comment(post_id: int, comment: CommentCreate):
    """게시글에 댓글 추가"""
    # TODO: 구현하세요
    pass


@app.get("/posts/{post_id}/comments/")
def get_comments(post_id: int):
    """게시글의 댓글 목록"""
    # TODO: 구현하세요
    pass


# 테스트를 위한 초기 데이터
def init_test_data():
    """테스트용 초기 데이터 생성"""
    test_posts = [
        {"title": "FastAPI 소개", "content": "FastAPI는 정말 빠릅니다!", "author": "김철수", "category": "tech"},
        {"title": "Python 공부법", "content": "매일 조금씩 코딩하세요", "author": "이영희", "category": "study"},
        {"title": "주말 계획", "content": "등산 가실 분?", "author": "박민수", "category": "general"},
    ]
    
    for post_data in test_posts:
        post = PostCreate(**post_data)
        create_post(post)


@app.on_event("startup")
def startup_event():
    """서버 시작 시 테스트 데이터 생성"""
    # init_test_data()  # 필요시 주석 해제
    pass


if __name__ == "__main__":
    print("""
    게시판 API 과제
    
    1. 모든 TODO 부분을 구현하세요
    2. 서버 실행: uvicorn homework:app --reload
    3. http://localhost:8000/docs 에서 테스트
    
    구현 팁:
    - PostResponse에 Config 클래스 추가 필요
    - 404 에러는 HTTPException 사용
    - 검색 기능은 in 연산자 활용
    - 정렬은 sorted() 함수 사용
    """)
