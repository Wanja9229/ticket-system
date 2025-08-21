## main.py
### 전역 함수
from member_manager import MemberManager

def main():
    print("=====회원 시스템에 오신 것을 환영합니다=====")
    member = MemberManager()
    member.run()

if __name__ == '__main__':
    main()


