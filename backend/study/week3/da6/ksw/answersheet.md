# 📚 초급자용 도서관 시스템 - 상세 구현

## 🎯 학습 목표
- 클래스 기본 개념 이해
- 객체 간의 관계 이해 (책 ↔ 회원 ↔ 도서관)
- 리스트로 객체 관리하기

---

## 📝 Step 1: 기본 뼈대 코드

```python
from datetime import datetime

class Book:
    """책 클래스 - 책 한 권의 정보"""
    
    def __init__(self, title, author, isbn):
        """책 생성자"""
        self.title = title          # 책 제목
        self.author = author        # 저자
        self.isbn = isbn            # ISBN (책 고유번호)
        self.is_available = True    # 대출 가능 여부
        self.borrowed_by = None     # 누가 빌렸는지
        self.borrowed_date = None   # 언제 빌렸는지
    
    def __str__(self):
        """책 정보를 문자열로 표현"""
        if self.is_available:
            status = "✅ 대출 가능"
        else:
            status = f"❌ 대출중 ({self.borrowed_by}님)"
        
        return f"📖 [{self.isbn}] {self.title} - {self.author} | {status}"


class Member:
    """회원 클래스 - 도서관 회원"""
    
    def __init__(self, name, member_id):
        """회원 생성자"""
        self.name = name                # 회원 이름
        self.member_id = member_id      # 회원 ID
        self.borrowed_books = []        # 빌린 책 리스트
        self.max_books = 3              # 최대 대출 가능 권수
        self.join_date = datetime.now() # 가입일
    
    def can_borrow(self):
        """대출 가능한지 확인"""
        return len(self.borrowed_books) < self.max_books
    
    def show_borrowed_books(self):
        """내가 빌린 책 목록 보기"""
        if not self.borrowed_books:
            return f"{self.name}님은 대출한 책이 없습니다."
        
        result = f"\n📚 {self.name}님의 대출 목록:\n"
        result += "-" * 50 + "\n"
        for i, book in enumerate(self.borrowed_books, 1):
            result += f"{i}. {book.title} - {book.author}\n"
        result += f"\n총 {len(self.borrowed_books)}권 대출중 (한도: {self.max_books}권)"
        return result
    
    def __str__(self):
        """회원 정보를 문자열로 표현"""
        return f"👤 [{self.member_id}] {self.name} | 대출: {len(self.borrowed_books)}/{self.max_books}권"


class Library:
    """도서관 클래스 - 전체 시스템 관리"""
    
    def __init__(self, name):
        """도서관 생성자"""
        self.name = name        # 도서관 이름
        self.books = []         # 모든 책 리스트
        self.members = []       # 모든 회원 리스트
        
        # 초기 데이터 추가
        self.add_sample_data()
    
    def add_sample_data(self):
        """샘플 데이터 추가"""
        # 샘플 책 추가
        sample_books = [
            ("파이썬 기초", "김파이", "001"),
            ("자바 입문", "이자바", "002"),
            ("웹 개발의 정석", "박웹", "003"),
            ("알고리즘 쉽게 배우기", "최알고", "004"),
            ("데이터베이스 첫걸음", "정디비", "005")
        ]
        
        for title, author, isbn in sample_books:
            self.add_book(Book(title, author, isbn))
        
        # 샘플 회원 추가
        sample_members = [
            ("김철수", "M001"),
            ("이영희", "M002"),
            ("박민수", "M003")
        ]
        
        for name, member_id in sample_members:
            self.add_member(Member(name, member_id))
        
        print(f"✨ '{self.name}'에 샘플 데이터가 추가되었습니다!")
        print(f"   - 책 {len(self.books)}권")
        print(f"   - 회원 {len(self.members)}명\n")
    
    def add_book(self, book):
        """책 추가"""
        self.books.append(book)
    
    def add_member(self, member):
        """회원 추가"""
        self.members.append(member)
    
    def find_book(self, search_term):
        """책 검색 (제목 또는 ISBN)"""
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term == book.isbn:
                return book
        return None
    
    def find_member(self, search_term):
        """회원 검색 (이름 또는 ID)"""
        for member in self.members:
            if search_term in member.name or search_term == member.member_id:
                return member
        return None
    
    def show_all_books(self):
        """모든 책 목록 보기"""
        print(f"\n📚 {self.name} 도서 목록")
        print("=" * 60)
        
        # 대출 가능한 책
        available_books = [b for b in self.books if b.is_available]
        borrowed_books = [b for b in self.books if not b.is_available]
        
        if available_books:
            print("\n✅ 대출 가능한 책:")
            for book in available_books:
                print(f"  {book}")
        
        if borrowed_books:
            print("\n❌ 대출중인 책:")
            for book in borrowed_books:
                print(f"  {book}")
        
        print(f"\n총 {len(self.books)}권 (대출가능: {len(available_books)}권)")
        print("=" * 60)
    
    def show_all_members(self):
        """모든 회원 목록 보기"""
        print(f"\n👥 {self.name} 회원 목록")
        print("=" * 60)
        for member in self.members:
            print(f"  {member}")
        print(f"\n총 {len(self.members)}명")
        print("=" * 60)
    
    def borrow_book(self, member_id, book_isbn):
        """책 대출하기"""
        # 회원 찾기
        member = self.find_member(member_id)
        if not member:
            return "❌ 회원을 찾을 수 없습니다."
        
        # 책 찾기
        book = self.find_book(book_isbn)
        if not book:
            return "❌ 책을 찾을 수 없습니다."
        
        # 대출 가능 여부 확인
        if not book.is_available:
            return f"❌ '{book.title}'은(는) 이미 대출중입니다."
        
        if not member.can_borrow():
            return f"❌ {member.name}님은 대출 한도({member.max_books}권)에 도달했습니다."
        
        # 대출 처리
        book.is_available = False
        book.borrowed_by = member.name
        book.borrowed_date = datetime.now().strftime("%Y-%m-%d")
        member.borrowed_books.append(book)
        
        return f"✅ {member.name}님이 '{book.title}'을(를) 대출했습니다!"
    
    def return_book(self, member_id, book_isbn):
        """책 반납하기"""
        # 회원 찾기
        member = self.find_member(member_id)
        if not member:
            return "❌ 회원을 찾을 수 없습니다."
        
        # 책 찾기
        book = self.find_book(book_isbn)
        if not book:
            return "❌ 책을 찾을 수 없습니다."
        
        # 반납 가능 여부 확인
        if book not in member.borrowed_books:
            return f"❌ {member.name}님은 '{book.title}'을(를) 대출하지 않았습니다."
        
        # 반납 처리
        book.is_available = True
        book.borrowed_by = None
        book.borrowed_date = None
        member.borrowed_books.remove(book)
        
        return f"✅ {member.name}님이 '{book.title}'을(를) 반납했습니다!"


def main():
    """메인 실행 함수"""
    # 도서관 생성
    library = Library("중앙 도서관")
    
    while True:
        print("\n" + "="*60)
        print(f"📚 {library.name} 관리 시스템")
        print("="*60)
        print("1. 📖 도서 목록 보기")
        print("2. 👥 회원 목록 보기")
        print("3. 📤 책 대출하기")
        print("4. 📥 책 반납하기")
        print("5. 🔍 내 대출 목록 보기")
        print("6. ➕ 새 책 추가하기")
        print("7. ➕ 새 회원 등록하기")
        print("0. 🚪 종료")
        print("-"*60)
        
        choice = input("\n메뉴를 선택하세요: ")
        
        if choice == "1":
            # 도서 목록
            library.show_all_books()
            
        elif choice == "2":
            # 회원 목록
            library.show_all_members()
            
        elif choice == "3":
            # 책 대출
            print("\n📤 책 대출하기")
            member_id = input("회원 ID 입력 (예: M001): ")
            book_isbn = input("책 ISBN 입력 (예: 001): ")
            result = library.borrow_book(member_id, book_isbn)
            print(result)
            
        elif choice == "4":
            # 책 반납
            print("\n📥 책 반납하기")
            member_id = input("회원 ID 입력: ")
            book_isbn = input("책 ISBN 입력: ")
            result = library.return_book(member_id, book_isbn)
            print(result)
            
        elif choice == "5":
            # 내 대출 목록
            print("\n🔍 대출 목록 조회")
            member_id = input("회원 ID 입력: ")
            member = library.find_member(member_id)
            if member:
                print(member.show_borrowed_books())
            else:
                print("❌ 회원을 찾을 수 없습니다.")
                
        elif choice == "6":
            # 새 책 추가
            print("\n➕ 새 책 추가")
            title = input("책 제목: ")
            author = input("저자: ")
            isbn = input("ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print(f"✅ '{title}' 책이 추가되었습니다!")
            
        elif choice == "7":
            # 새 회원 등록
            print("\n➕ 새 회원 등록")
            name = input("이름: ")
            member_id = input("회원 ID: ")
            new_member = Member(name, member_id)
            library.add_member(new_member)
            print(f"✅ {name}님이 회원으로 등록되었습니다!")
            
        elif choice == "0":
            print("\n👋 프로그램을 종료합니다. 안녕히 가세요!")
            break
            
        else:
            print("❌ 잘못된 선택입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()
```

---

## 🎯 핵심 개념 설명

### 1. **클래스란?**
```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title      # 속성(데이터)
        self.author = author    # 속성(데이터)
```
- 클래스 = 설계도 (붕어빵 틀)
- 객체 = 실제 만들어진 것 (붕어빵)

### 2. **객체 생성과 사용**
```python
# 객체 생성
book1 = Book("파이썬 기초", "김파이", "001")

# 객체 사용
print(book1.title)  # "파이썬 기초" 출력
book1.is_available = False  # 속성 변경
```

### 3. **메서드(함수)**
```python
def can_borrow(self):
    return len(self.borrowed_books) < self.max_books
```
- 클래스 안의 함수 = 메서드
- `self`는 자기 자신을 가리킴

### 4. **객체 간의 관계**
```python
# Library가 Book과 Member를 관리
library.books = [book1, book2, book3]
library.members = [member1, member2]

# Member가 Book을 빌림
member.borrowed_books = [book1, book2]
```

---

## 📝 실습 순서

### Step 1: 기본 실행
1. 코드 전체를 복사해서 실행
2. 메뉴 1번으로 책 목록 확인
3. 메뉴 2번으로 회원 목록 확인

### Step 2: 대출/반납 테스트
1. 메뉴 3번: 책 대출
   - 회원 ID: M001
   - ISBN: 001
2. 메뉴 1번으로 대출 상태 확인
3. 메뉴 5번으로 김철수의 대출 목록 확인

### Step 3: 새 데이터 추가
1. 메뉴 6번: 새 책 추가
2. 메뉴 7번: 새 회원 추가
3. 추가한 회원으로 책 대출 테스트

---

## 💡 확장 아이디어 (도전 과제)

### 초급 도전 과제
1. **연체 기능 추가**
   ```python
   # Book 클래스에 추가
   def is_overdue(self):
       # 14일 이상 대출시 연체
       pass
   ```

2. **책 검색 기능 개선**
   ```python
   # 저자로도 검색 가능하게
   def find_book_by_author(self, author_name):
       pass
   ```

3. **통계 기능**
   ```python
   # 가장 인기있는 책, 가장 많이 빌린 회원 등
   def show_statistics(self):
       pass
   ```

### 중급 도전 과제
1. **VIP 회원 클래스 추가**
   ```python
   class VIPMember(Member):
       def __init__(self, name, member_id):
           super().__init__(name, member_id)
           self.max_books = 5  # 더 많이 빌릴 수 있음
   ```

2. **책 카테고리 추가**
   ```python
   class Book:
       def __init__(self, title, author, isbn, category):
           # IT, 소설, 자기계발 등
   ```

---

## 🎮 테스트 시나리오

### 시나리오 1: 대출 한도 테스트
1. 김철수(M001)로 책 3권 대출
2. 4번째 책 대출 시도 → 실패 메시지 확인

### 시나리오 2: 중복 대출 방지
1. 김철수가 001번 책 대출
2. 이영희가 같은 001번 책 대출 시도 → 실패

### 시나리오 3: 반납 테스트
1. 김철수가 빌린 책 반납
2. 다른 사람이 그 책 대출 가능한지 확인