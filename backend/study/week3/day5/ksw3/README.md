# 📚 Python 클래스 상속 & 오버라이딩 실습 프로젝트

## 🎯 프로젝트 개요
게시판 시스템을 구현하며 클래스 상속과 오버라이딩을 학습하는 프로젝트

---

## 📋 1차 목표: 게시글 & 공지사항 시스템

### 구현 사항
- ✅ Post 클래스 (기본 게시글 CRUD)
- ✅ Notice 클래스 (Post 상속, 공지사항 기능)
- ✅ 오버라이딩: `write()`, `show()` 메서드
- ✅ JSON 파일 저장/불러오기

### 클래스 구조
```
Post (기본 게시글)
 └── Notice (공지사항) - Post를 상속
     └── is_notice 속성 추가
     └── write() 오버라이딩 (공지 설정 여부 묻기)
     └── show() 오버라이딩 (공지 스타일 출력)
```

---

## 💻 1차 뼈대 코드

```python
import json
from datetime import datetime

class Post:
    """기본 게시글 클래스"""
    post_id = 1  # 클래스 변수로 ID 관리
    
    def __init__(self, title="", content="", author=""):
        # TODO: 필요한 속성들 초기화
        # id, title, content, author, created_at, views 등
        pass
    
    def write(self):
        """게시글 작성 - 입력받기"""
        # TODO: input()으로 제목, 내용, 작성자 입력받기
        # self.title, self.content, self.author에 저장
        # 작성 완료 메시지 출력
        pass
    
    def show(self):
        """게시글 조회"""
        # TODO: 조회수 증가
        # 게시글 정보 출력 (번호, 제목, 작성자, 작성일, 조회수, 내용)
        pass
    
    def update(self):
        """게시글 수정"""
        # TODO: 현재 제목/내용 보여주고
        # 새로운 제목/내용 입력받기 (엔터시 기존값 유지)
        pass
    
    def to_dict(self):
        """딕셔너리로 변환 (JSON 저장용)"""
        # TODO: 객체의 속성들을 딕셔너리로 변환
        # type: 'post' 포함시키기
        pass
    
    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 객체 생성 (JSON 로드용)"""
        # TODO: 딕셔너리 데이터로 Post 객체 생성
        pass


class Notice(Post):
    """공지사항 클래스 (Post 상속)"""
    
    def __init__(self, title="", content="", author=""):
        # TODO: super()로 부모 생성자 호출
        # is_notice = True, is_pinned = True 추가
        pass
    
    def write(self):
        """공지사항 작성 - 오버라이딩"""
        # TODO: super().write() 활용
        # 공지로 설정할지 묻기 (y/n)
        # is_notice 설정
        pass
    
    def show(self):
        """공지사항 조회 - 오버라이딩"""
        # TODO: 공지사항 스타일로 출력
        # 📢 이모지, 테두리, 고정 상태 표시
        # 조회수는 부모와 동일하게 증가
        pass
    
    def to_dict(self):
        """딕셔너리로 변환 - 오버라이딩"""
        # TODO: super().to_dict() 호출해서 기본 데이터 받고
        # type: 'notice', is_notice, is_pinned 추가
        pass


class Board:
    """게시판 관리 클래스"""
    
    def __init__(self):
        # TODO: self.posts = {} 초기화
        # load_data() 호출
        pass
    
    def add_post(self, post):
        """게시글 추가"""
        # TODO: self.posts에 추가
        # save_data() 호출
        pass
    
    def list_posts(self):
        """게시글 목록 출력"""
        # TODO: 공지사항과 일반글 분리
        # isinstance() 활용
        # 공지 먼저, 일반글 나중에 출력
        pass
    
    def get_post(self, post_id):
        """특정 게시글 조회"""
        # TODO: self.posts에서 해당 id 찾기
        pass
    
    def delete_post(self, post_id):
        """게시글 삭제"""
        # TODO: 해당 id 삭제
        # save_data() 호출
        pass
    
    def save_data(self):
        """JSON 파일로 저장"""
        # TODO: self.posts를 리스트로 변환
        # json.dump()로 저장
        pass
    
    def load_data(self):
        """JSON 파일에서 불러오기"""
        # TODO: json.load()로 읽기
        # type에 따라 Post 또는 Notice 객체 생성
        # FileNotFoundError 처리
        pass


def main():
    """메인 실행 함수"""
    board = Board()
    
    while True:
        # TODO: 메뉴 출력
        # 1. 게시글 작성
        # 2. 공지사항 작성  
        # 3. 게시글 목록
        # 4. 게시글 읽기
        # 5. 게시글 수정
        # 6. 게시글 삭제
        # 0. 종료
        
        choice = input("선택: ")
        
        # TODO: 각 메뉴별 기능 구현
        pass


if __name__ == "__main__":
    main()
```

---

## 📁 예시 JSON 데이터

`board_data.json`:
```json
[
  {
    "id": 1,
    "type": "notice",
    "title": "🎉 게시판 오픈 공지",
    "content": "새로운 게시판이 오픈되었습니다.",
    "author": "관리자",
    "created_at": "2024-12-26 10:00:00",
    "views": 15,
    "is_notice": true,
    "is_pinned": true
  },
  {
    "id": 2,
    "type": "post",
    "title": "안녕하세요",
    "content": "처음 가입했습니다.",
    "author": "김철수",
    "created_at": "2024-12-26 11:30:00",
    "views": 3
  },
  {
    "id": 3,
    "type": "post",
    "title": "질문있습니다",
    "content": "게시판 사용법이 궁금해요",
    "author": "이영희",
    "created_at": "2024-12-26 14:20:00",
    "views": 7
  }
]
```

---

## 📋 2차 목표: 사용자 권한 시스템

### 구현 사항
- ✅ User 클래스 (권한 체크 기능)
- ✅ Admin 클래스 (User 상속, 전체 권한)
- ✅ 오버라이딩: `auth_check()` 메서드
- ✅ 게시글과 사용자 연동

---

## 💻 2차 뼈대 코드

```python
class User:
    """사용자 클래스"""
    
    def __init__(self, username, password):
        # TODO: username, password, created_at 초기화
        pass
    
    def auth_check(self, action, target=None):
        """권한 체크 메서드"""
        # TODO: action별 권한 체크
        # "edit": 본인 글만 (target.author == self.username)
        # "delete": 본인 글만
        # "write_notice": False (일반 유저는 공지 작성 불가)
        pass


class Admin(User):
    """관리자 클래스 (User 상속)"""
    
    def __init__(self, username, password):
        # TODO: super()로 부모 생성자 호출
        # is_admin = True 추가
        pass
    
    def auth_check(self, action, target=None):
        """권한 체크 - 오버라이딩"""
        # TODO: 모든 권한 True 반환
        pass


# Post 클래스 수정 사항
class Post:
    def __init__(self, title="", content="", author=None):
        # TODO: author를 User 객체로 받도록 수정
        pass
    
    def edit(self, user):
        """사용자 권한 체크 후 수정"""
        # TODO: user.auth_check("edit", self) 호출
        # 권한 있으면 update() 실행
        # 없으면 권한 없음 메시지
        pass
    
    def delete(self, user):
        """사용자 권한 체크 후 삭제"""
        # TODO: user.auth_check("delete", self) 호출
        # 권한 체크 후 처리
        pass
```

---

## 🎯 구현 순서

### 1차 구현
1. Post 클래스의 기본 메서드들 완성
2. Notice 클래스의 오버라이딩 메서드 구현
3. Board 클래스로 게시글 관리
4. main() 함수에서 메뉴 시스템 구현
5. JSON 저장/불러오기 테스트

### 2차 구현
1. User 클래스와 auth_check() 구현
2. Admin 클래스 상속 및 오버라이딩
3. Post의 author를 User 객체로 변경
4. 권한 체크 기능 연동
5. 로그인 시스템 추가 (선택)

---

## 💡 핵심 학습 포인트

### 상속 (Inheritance)
- `class Notice(Post):` - Notice가 Post 상속
- `super().__init__()` - 부모 생성자 호출
- 부모의 모든 메서드와 속성 사용 가능

### 오버라이딩 (Overriding)
- **Notice.write()** - 공지 설정 추가
- **Notice.show()** - 다른 출력 스타일
- **Admin.auth_check()** - 모든 권한 허용

### 다형성 (Polymorphism)
```python
# 같은 show() 호출이지만 객체 타입에 따라 다르게 동작
for post in posts:
    post.show()  # Post면 일반 출력, Notice면 공지 출력
```

---

## 📝 테스트 시나리오

### 1차 테스트
1. 일반 게시글 2개 작성
2. 공지사항 1개 작성
3. 목록 확인 (공지가 위에 표시되는지)
4. 각각 읽기 (다른 스타일로 출력되는지)
5. 프로그램 재시작 후 데이터 유지 확인

### 2차 테스트
1. 일반 유저로 로그인
2. 본인 글 수정 (성공)
3. 타인 글 수정 시도 (실패)
4. 관리자로 로그인
5. 모든 글 수정 가능 확인
6. 공지사항 작성 권한 확인