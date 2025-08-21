
def menu_pop():
    print('====메뉴선택====')
    print('1. 회원가입')
    print('2. 전체회원조회')
    print('3. 회원조회')
    print('4. 회원수정')
    print('5. 회원삭제')
    print('6. 파일저장')
    print('7. 프로그램종료')

def menu_input():
    try:
        menu_num = int(input('실행할 메뉴를 입력해주세요 : ').strip())
        if 1<= menu_num <=7:
            return menu_num
        else:
            print('메뉴 번호를 확인해주세요')
            return 0
    except ValueError:
        print('번호를 입력해주세요')