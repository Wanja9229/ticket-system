# main.py - 메인 실행 파일
from member_manager import MemberManager

def main():
    """메인 함수"""
    print("회원 관리 시스템에 오신 것을 환영합니다!")
    
    manager = MemberManager()
    manager.run()

if __name__ == "__main__":
    main()