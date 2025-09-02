from datetime import datetime
from typing import Optional, List

# ============================================================
# 도서 클래스들 (상속 구조)
# ============================================================

class Book:
    """기본 책 클래스 - 모든 도서의 부모 클래스"""
    
    def __init__(self, title: str, author: str, isbn: str):
        """책 객체 초기화"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available: bool = True
        self.borrowed_by: Optional[str] = None
        self.borrowed_date: Optional[datetime] = None
    
    def get_loan_period(self) -> int:
        """대출 기간 (일) - 자식 클래스에서 오버라이딩 가능"""
        return 14  # 기본 2주
    
    def get_book_type(self) -> str:
        """책 타입 반환"""
        return "일반도서"
    
    def __str__(self):
        """책 정보를 문자열로 반환"""
        if self.is_available:
            status = "✅ 대출 가능"
        else:
            status = f"❌ 대출중 ({self.borrowed_by}님)"
        
        return f"📖 [{self.isbn}] {self.title} - {self.author} | {self.get_book_type()} | {status}"


class EBook(Book):
    """전자책 클래스 - Book을 상속"""
    
    def __init__(self, title: str, author: str, isbn: str, file_size: float):
        super().__init__(title, author, isbn)  # 부모 클래스 초기화
        self.file_size = file_size  # MB 단위
        self.download_count = 0
    
    def get_loan_period(self) -> int:
        """전자책은 대출 기간이 짧음 (오버라이딩)"""
        return 7  # 1주
    
    def get_book_type(self) -> str:
        """책 타입 반환 (오버라이딩)"""
        return f"전자책({self.file_size}MB)"
    
    def download(self) -> str:
        """전자책 다운로드 - 전자책만의 메서드"""
        self.download_count += 1
        return f"💾 '{self.title}' 다운로드 완료! (다운로드 횟수: {self.download_count})"


class AudioBook(Book):
    """오디오북 클래스 - Book을 상속"""
    
    def __init__(self, title: str, author: str, isbn: str, duration: int, narrator: str):
        super().__init__(title, author, isbn)
        self.duration = duration  # 분 단위
        self.narrator = narrator  # 낭독자
    
    def get_loan_period(self) -> int:
        """오디오북 대출 기간 (오버라이딩)"""
        return 21  # 3주
    
    def get_book_type(self) -> str:
        """책 타입 반환 (오버라이딩)"""
        hours = self.duration // 60
        minutes = self.duration % 60
        return f"오디오북({hours}시간 {minutes}분)"
    
    def get_narrator_info(self) -> str:
        """낭독자 정보 - 오디오북만의 메서드"""
        return f"🎙️ 낭독: {self.narrator}"


# ============================================================
# 회원 클래스들 (상속 구조)
# ============================================================

class Member:
    """기본 회원 클래스 - 모든 회원의 부모 클래스"""
    
    def __init__(self, name: str, member_id: str):
        """회원 객체 초기화"""
        self.name = name
        self.member_id = member_id
        self.borrowed_books: List[Book] = []
        self.max_books: int = 3  # 일반 회원은 3권
        self.join_date: datetime = datetime.now()
    
    def can_borrow(self) -> bool:
        """대출 가능 여부 확인"""
        return len(self.borrowed_books) < self.max_books
    
    def get_membership_type(self) -> str:
        """회원 등급 반환"""
        return "일반회원"
    
    def get_late_fee_per_day(self) -> int:
        """하루 연체료"""
        return 500  # 일반 회원 500원
    
    def show_borrowed_books(self) -> str:
        """내가 빌린 책 목록을 문자열로 반환"""
        if not self.borrowed_books:
            return f"{self.name}님은 대출한 책이 없습니다."
        
        result = f"\n📚 {self.name}님의 대출 목록 ({self.get_membership_type()}):\n"
        result += "-" * 50 + "\n"
        for i, book in enumerate(self.borrowed_books, 1):
            result += f"{i}. {book.title} - {book.author} ({book.get_book_type()})\n"
        result += f"\n총 {len(self.borrowed_books)}권 대출중 (한도: {self.max_books}권)"
        return result
    
    def __str__(self):
        """회원 정보를 문자열로 반환"""
        return f"👤 [{self.member_id}] {self.name} | {self.get_membership_type()} | 대출: {len(self.borrowed_books)}/{self.max_books}권"


class VIPMember(Member):
    """VIP 회원 클래스 - Member를 상속"""
    
    def __init__(self, name: str, member_id: str):
        super().__init__(name, member_id)
        self.max_books: int = 5  # VIP는 5권까지
        self.point: int = 0  # VIP 포인트
    
    def get_membership_type(self) -> str:
        """회원 등급 반환 (오버라이딩)"""
        return "⭐ VIP회원"
    
    def get_late_fee_per_day(self) -> int:
        """VIP는 연체료 할인 (오버라이딩)"""
        return 300  # VIP는 300원
    
    def add_point(self, amount: int) -> str:
        """포인트 적립 - VIP만의 메서드"""
        self.point += amount
        return f"💰 {amount}포인트 적립! (현재: {self.point}P)"


class StudentMember(Member):
    """학생 회원 클래스 - Member를 상속"""
    
    def __init__(self, name: str, member_id: str, school: str, grade: int):
        super().__init__(name, member_id)
        self.max_books: int = 5  # 학생은 5권까지
        self.school = school  # 학교명
        self.grade = grade    # 학년
    
    def get_membership_type(self) -> str:
        """회원 등급 반환 (오버라이딩)"""
        return f"🎓 학생회원({self.school})"
    
    def get_late_fee_per_day(self) -> int:
        """학생은 연체료 감면 (오버라이딩)"""
        return 200  # 학생은 200원
    
    def get_student_info(self) -> str:
        """학생 정보 - 학생회원만의 메서드"""
        return f"📚 {self.school} {self.grade}학년"


# ============================================================
# 도서관 클래스 (상속된 클래스들을 모두 관리)
# ============================================================

class Library:
    """도서관 클래스 - 전체 시스템을 관리"""
    
    def __init__(self, name: str):
        """도서관 객체 초기화"""
        self.name = name
        self.books: List[Book] = []
        self.members: List[Member] = []
        
        # 초기 데이터 추가
        self.add_sample_data()
    
    def add_sample_data(self):
        """테스트용 샘플 데이터 추가 - 다양한 타입의 책과 회원"""
        
        # 다양한 타입의 책 추가
        books_data = [
            Book("파이썬 기초", "김파이", "001"),
            Book("자바 입문", "이자바", "002"),
            EBook("웹 개발의 정석", "박웹", "003", 15.5),
            AudioBook("알고리즘 쉽게 배우기", "최알고", "004", 240, "정낭독"),
            EBook("데이터베이스 첫걸음", "정디비", "005", 8.2),
            AudioBook("영어회화 마스터", "김영어", "006", 180, "이낭독")
        ]
        
        for book in books_data:
            self.add_book(book)
        
        # 다양한 타입의 회원 추가
        members_data = [
            Member("김철수", "M001"),
            VIPMember("이영희", "V001"),
            StudentMember("박민수", "S001", "서울대", 3),
            VIPMember("최부자", "V002"),
            StudentMember("정학생", "S002", "연세대", 2)
        ]
        
        for member in members_data:
            self.add_member(member)
        
        print(f"✨ '{self.name}'에 샘플 데이터가 추가되었습니다!")
        print(f"   - 책 {len(self.books)}권 (일반: 2, 전자책: 2, 오디오북: 2)")
        print(f"   - 회원 {len(self.members)}명 (일반: 1, VIP: 2, 학생: 2)\n")
    
    def add_book(self, book: Book):
        """새 책 추가"""
        self.books.append(book)
    
    def add_member(self, member: Member):
        """새 회원 추가"""
        self.members.append(member)
    
    def find_book(self, search_term: str) -> Optional[Book]:
        """책 검색 (제목 또는 ISBN으로 검색)"""
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term == book.isbn:
                return book
        return None
    
    def find_member(self, search_term: str) -> Optional[Member]:
        """회원 검색 (이름 또는 ID로 검색)"""
        for member in self.members:
            if search_term in member.name or search_term == member.member_id:
                return member
        return None
    
    def show_all_books(self):
        """모든 책 목록 출력 - 타입별로 구분"""
        print(f"\n📚 {self.name} 도서 목록")
        print("=" * 70)
        
        # 타입별로 분류
        normal_books = [b for b in self.books if type(b) == Book]
        ebooks = [b for b in self.books if isinstance(b, EBook)]
        audiobooks = [b for b in self.books if isinstance(b, AudioBook)]
        
        if normal_books:
            print("\n📖 일반 도서:")
            for book in normal_books:
                print(f"  {book}")
        
        if ebooks:
            print("\n💾 전자책:")
            for book in ebooks:
                print(f"  {book}")
        
        if audiobooks:
            print("\n🎧 오디오북:")
            for book in audiobooks:
                print(f"  {book}")
                if isinstance(book, AudioBook):
                    print(f"     └─ {book.get_narrator_info()}")
        
        # 대출 통계
        available = len([b for b in self.books if b.is_available])
        borrowed = len(self.books) - available
        
        print(f"\n📊 통계: 총 {len(self.books)}권 (대출가능: {available}권, 대출중: {borrowed}권)")
        print("=" * 70)
    
    def show_all_members(self):
        """모든 회원 목록 출력 - 등급별로 구분"""
        print(f"\n👥 {self.name} 회원 목록")
        print("=" * 70)
        
        # 등급별로 분류
        regular = [m for m in self.members if type(m) == Member]
        vip = [m for m in self.members if isinstance(m, VIPMember)]
        students = [m for m in self.members if isinstance(m, StudentMember)]
        
        if vip:
            print("\n⭐ VIP 회원:")
            for member in vip:
                print(f"  {member}")
        
        if students:
            print("\n🎓 학생 회원:")
            for member in students:
                print(f"  {member}")
                print(f"     └─ {member.get_student_info()}")
        
        if regular:
            print("\n👤 일반 회원:")
            for member in regular:
                print(f"  {member}")
        
        print(f"\n📊 통계: 총 {len(self.members)}명 (VIP: {len(vip)}, 학생: {len(students)}, 일반: {len(regular)})")
        print("=" * 70)
    
    def borrow_book(self, member_id: str, book_isbn: str) -> str:
        """책 대출 처리"""
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
        book.borrowed_date = datetime.now()
        member.borrowed_books.append(book)
        
        # VIP 회원은 포인트 적립
        bonus_msg = ""
        if isinstance(member, VIPMember):
            bonus_msg = f"\n   {member.add_point(10)}"
        
        return f"✅ {member.name}님({member.get_membership_type()})이 '{book.title}'을(를) 대출했습니다!\n   대출기간: {book.get_loan_period()}일{bonus_msg}"
    
    def return_book(self, member_id: str, book_isbn: str) -> str:
        """책 반납 처리"""
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
        
        # 연체 일수 계산
        if book.borrowed_date:
            days_borrowed = (datetime.now() - book.borrowed_date).days
            if days_borrowed > book.get_loan_period():
                late_days = days_borrowed - book.get_loan_period()
                late_fee = late_days * member.get_late_fee_per_day()
                late_msg = f"\n   ⚠️ 연체 {late_days}일 - 연체료: {late_fee}원"
            else:
                late_msg = ""
        else:
            late_msg = ""
        
        # 반납 처리
        book.is_available = True
        book.borrowed_by = None
        book.borrowed_date = None
        member.borrowed_books.remove(book)
        
        return f"✅ {member.name}님이 '{book.title}'을(를) 반납했습니다!{late_msg}"


def main():
    """메인 실행 함수"""
    # 도서관 생성
    library = Library("중앙 도서관")
    
    while True:
        print("\n" + "="*70)
        print(f"📚 {library.name} 관리 시스템 (상속 버전)")
        print("="*70)
        print("1. 📖 도서 목록 보기 (타입별)")
        print("2. 👥 회원 목록 보기 (등급별)")
        print("3. 📤 책 대출하기")
        print("4. 📥 책 반납하기")
        print("5. 🔍 내 대출 목록 보기")
        print("6. ➕ 새 책 추가하기")
        print("7. ➕ 새 회원 등록하기")
        print("8. 💾 전자책 다운로드")
        print("9. 📊 회원 타입별 혜택 보기")
        print("0. 🚪 종료")
        print("-"*70)
        
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
            member_id = input("회원 ID 입력 (예: M001, V001, S001): ")
            book_isbn = input("책 ISBN 입력 (예: 001~006): ")
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
                # 학생 회원이면 추가 정보
                if isinstance(member, StudentMember):
                    print(f"\n   {member.get_student_info()}")
            else:
                print("❌ 회원을 찾을 수 없습니다.")
                
        elif choice == "6":
            # 새 책 추가
            print("\n➕ 새 책 추가")
            print("책 타입 선택: 1.일반책  2.전자책  3.오디오북")
            book_type = input("선택: ")
            
            title = input("책 제목: ")
            author = input("저자: ")
            isbn = input("ISBN: ")
            
            if book_type == "2":
                file_size = float(input("파일 크기(MB): "))
                new_book = EBook(title, author, isbn, file_size)
            elif book_type == "3":
                duration = int(input("재생 시간(분): "))
                narrator = input("낭독자: ")
                new_book = AudioBook(title, author, isbn, duration, narrator)
            else:
                new_book = Book(title, author, isbn)
            
            library.add_book(new_book)
            print(f"✅ '{title}' ({new_book.get_book_type()})이(가) 추가되었습니다!")
            
        elif choice == "7":
            # 새 회원 등록
            print("\n➕ 새 회원 등록")
            print("회원 타입: 1.일반  2.VIP  3.학생")
            member_type = input("선택: ")
            
            name = input("이름: ")
            member_id = input("회원 ID: ")
            
            if member_type == "2":
                new_member = VIPMember(name, member_id)
            elif member_type == "3":
                school = input("학교명: ")
                grade = int(input("학년: "))
                new_member = StudentMember(name, member_id, school, grade)
            else:
                new_member = Member(name, member_id)
            
            library.add_member(new_member)
            print(f"✅ {name}님이 {new_member.get_membership_type()}으로 등록되었습니다!")
            
        elif choice == "8":
            # 전자책 다운로드
            print("\n💾 전자책 다운로드")
            isbn = input("전자책 ISBN 입력: ")
            book = library.find_book(isbn)
            
            if isinstance(book, EBook):
                print(book.download())
            else:
                print("❌ 해당 도서는 전자책이 아닙니다.")
                
        elif choice == "9":
            # 회원 타입별 혜택
            print("\n📊 회원 등급별 혜택")
            print("=" * 50)
            print("👤 일반 회원: 대출 3권, 연체료 500원/일")
            print("⭐ VIP 회원: 대출 5권, 연체료 300원/일, 포인트 적립")
            print("🎓 학생 회원: 대출 5권, 연체료 200원/일")
            print("=" * 50)
            
        elif choice == "0":
            print("\n👋 프로그램을 종료합니다. 안녕히 가세요!")
            break
            
        else:
            print("❌ 잘못된 선택입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()