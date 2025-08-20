def menu_pop():
    print('======회원 관리 시스템======')
    print('1. 회원 가입')
    print('2. 전체 목록')
    print('3. 회원 조회')
    print('4. 회원 수정')
    print('5. 회원 삭제')
    print('6. 변경 저장')
    print('7. 프로그램 종료')
    print('===========================')
    print('실행할 메뉴의 숫자를 입력해 주세요.')
    

def menu_choice() -> int:
    try:
        choice = int(input("메뉴 선택 : "))

        if 1<= choice <= 7:
            return choice
        else:
            print('메뉴 번호를 확인해주세요.')
            return 0
    except ValueError:
        print('실행할 메뉴의 숫자를 입력해 주세요.')
        return 0