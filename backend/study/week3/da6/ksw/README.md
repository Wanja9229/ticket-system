📚 도서관 시스템 - 뼈대 코드 (직접 구현용)
🎯 구현 목표
아래 클래스와 메서드를 보고 직접 구현해보세요!

📝 뼈대 코드
pythonfrom datetime import datetime

class Book:
    """책 클래스 - 책 한 권의 정보를 관리"""
    
    def __init__(self, title, author, isbn):
        """
        책 객체 초기화
        필요한 속성:
        - title: 책 제목
        - author: 저자
        - isbn: 책 고유번호
        - is_available: 대출 가능 여부 (기본값: True)
        - borrowed_by: 대출한 사람 이름 (기본값: None)
        - borrowed_date: 대출 날짜 (기본값: None)
        """
        pass
    
    def __str__(self):
        """
        책 정보를 문자열로 반환
        형식: "📖 [ISBN] 제목 - 저자 | 상태"
        상태는 대출가능/대출중(누구) 표시
        """
        pass


class Member:
    """회원 클래스 - 도서관 회원 정보를 관리"""
    
    def __init__(self, name, member_id):
        """
        회원 객체 초기화
        필요한 속성:
        - name: 회원 이름
        - member_id: 회원 ID
        - borrowed_books: 빌린 책 리스트 (기본값: 빈 리스트)
        - max_books: 최대 대출 가능 권수 (기본값: 3)
        - join_date: 가입일 (현재 날짜)
        """
        pass
    
    def can_borrow(self):
        """
        대출 가능 여부 확인
        반환: True(대출 가능) 또는 False(한도 초과)
        """
        pass
    
    def show_borrowed_books(self):
        """
        내가 빌린 책 목록을 문자열로 반환
        - 빌린 책이 없으면: "대출한 책이 없습니다" 메시지
        - 있으면: 책 목록과 대출 권수/한도 표시
        """
        pass
    
    def __str__(self):
        """
        회원 정보를 문자열로 반환
        형식: "👤 [ID] 이름 | 대출: 현재권수/최대권수"
        """
        pass


class Library:
    """도서관 클래스 - 전체 시스템을 관리"""
    
    def __init__(self, name):
        """
        도서관 객체 초기화
        필요한 속성:
        - name: 도서관 이름
        - books: 모든 책을 저장할 리스트
        - members: 모든 회원을 저장할 리스트
        
        초기화 후 add_sample_data() 호출
        """
        pass
    
    def add_sample_data(self):
        """
        테스트용 샘플 데이터 추가
        - 책 5권 추가 (Book 객체 생성해서 books 리스트에 추가)
        - 회원 3명 추가 (Member 객체 생성해서 members 리스트에 추가)
        """
        pass
    
    def add_book(self, book):
        """
        새 책 추가
        매개변수: book - Book 객체
        기능: books 리스트에 추가
        """
        pass
    
    def add_member(self, member):
        """
        새 회원 추가
        매개변수: member - Member 객체
        기능: members 리스트에 추가
        """
        pass
    
    def find_book(self, search_term):
        """
        책 검색 (제목 또는 ISBN으로 검색)
        매개변수: search_term - 검색어
        반환: 찾은 Book 객체 또는 None
        """
        pass
    
    def find_member(self, search_term):
        """
        회원 검색 (이름 또는 ID로 검색)
        매개변수: search_term - 검색어
        반환: 찾은 Member 객체 또는 None
        """
        pass
    
    def show_all_books(self):
        """
        모든 책 목록 출력
        - 대출 가능한 책과 대출중인 책 구분해서 출력
        - 총 권수 표시
        """
        pass
    
    def show_all_members(self):
        """
        모든 회원 목록 출력
        - 각 회원 정보 출력
        - 총 회원수 표시
        """
        pass
    
    def borrow_book(self, member_id, book_isbn):
        """
        책 대출 처리
        매개변수:
        - member_id: 회원 ID
        - book_isbn: 책 ISBN
        
        처리 순서:
        1. 회원 찾기 (없으면 에러 메시지)
        2. 책 찾기 (없으면 에러 메시지)
        3. 책 대출 가능 확인 (이미 대출중이면 에러)
        4. 회원 대출 한도 확인 (한도 초과면 에러)
        5. 대출 처리:
           - book.is_available = False
           - book.borrowed_by = 회원이름
           - book.borrowed_date = 현재날짜
           - member.borrowed_books에 책 추가
        
        반환: 성공/실패 메시지
        """
        pass
    
    def return_book(self, member_id, book_isbn):
        """
        책 반납 처리
        매개변수:
        - member_id: 회원 ID
        - book_isbn: 책 ISBN
        
        처리 순서:
        1. 회원 찾기 (없으면 에러 메시지)
        2. 책 찾기 (없으면 에러 메시지)
        3. 해당 회원이 그 책을 빌렸는지 확인
        4. 반납 처리:
           - book.is_available = True
           - book.borrowed_by = None
           - book.borrowed_date = None
           - member.borrowed_books에서 책 제거
        
        반환: 성공/실패 메시지
        """
        pass


def main():
    """
    메인 실행 함수
    
    구현할 메뉴:
    1. 도서 목록 보기 - library.show_all_books()
    2. 회원 목록 보기 - library.show_all_members()
    3. 책 대출하기 - 입력받고 library.borrow_book()
    4. 책 반납하기 - 입력받고 library.return_book()
    5. 내 대출 목록 보기 - member.show_borrowed_books()
    6. 새 책 추가하기 - Book 객체 생성 후 library.add_book()
    7. 새 회원 등록하기 - Member 객체 생성 후 library.add_member()
    0. 종료
    
    while 루프로 계속 실행
    """
    pass


if __name__ == "__main__":
    main()

📋 구현 체크리스트
Book 클래스

 __init__: 6개 속성 초기화
 __str__: 책 정보 문자열 반환

Member 클래스

 __init__: 5개 속성 초기화
 can_borrow(): 대출 가능 여부 확인
 show_borrowed_books(): 대출 목록 반환
 __str__: 회원 정보 문자열 반환

Library 클래스

 __init__: 도서관 초기화
 add_sample_data(): 샘플 데이터 추가
 add_book(): 책 추가
 add_member(): 회원 추가
 find_book(): 책 검색
 find_member(): 회원 검색
 show_all_books(): 책 목록 출력
 show_all_members(): 회원 목록 출력
 borrow_book(): 대출 처리
 return_book(): 반납 처리

main 함수

 메뉴 출력
 사용자 입력 처리
 각 메뉴별 기능 실행


💡 구현 힌트
힌트 1: 리스트에서 객체 찾기
pythonfor book in self.books:
    if 조건:
        return book
return None
힌트 2: 대출 가능 여부 확인
pythonif len(self.borrowed_books) < self.max_books:
    return True
return False
힌트 3: 현재 날짜 가져오기
pythonfrom datetime import datetime
datetime.now()  # 현재 시간
datetime.now().strftime("%Y-%m-%d")  # 문자열 형식
힌트 4: 리스트에서 제거
python리스트.remove(객체)  # 특정 객체 제거
리스트.append(객체)  # 객체 추가
힌트 5: 문자열 포맷팅
pythonf"이름: {self.name}, ID: {self.member_id}"

🎯 테스트 케이스
구현 후 다음을 테스트해보세요:

정상 대출: M001 회원이 001 책 대출
중복 대출 방지: 다른 회원이 001 책 대출 시도
한도 초과: 한 회원이 4권째 대출 시도
반납: 대출한 책 반납
잘못된 반납: 빌리지 않은 책 반납 시도
새 데이터: 새 책, 새 회원 추가


📚 샘플 데이터 예시
책 데이터

("파이썬 기초", "김파이", "001")
("자바 입문", "이자바", "002")
("웹 개발의 정석", "박웹", "003")
("알고리즘 쉽게 배우기", "최알고", "004")
("데이터베이스 첫걸음", "정디비", "005")

회원 데이터

("김철수", "M001")
("이영희", "M002")
("박민수", "M003")