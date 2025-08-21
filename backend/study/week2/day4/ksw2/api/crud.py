from datetime import datetime

from api.file import file_open, file_save
from api.input import date_input

member_data = file_open()

def member_input():
    print('---회원가입---')
    name = input('이름 등록해주세요 : ')
    birth = date_input('생일을 등록해주세요')
    password = input('비밀번호 등록해주세요 : '),
    now_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_mb = {
        'name' : name,
        'birth_date' : birth,
        'password' : password,
        'register_date' : now_datetime
    }

    member_data.append(new_mb)
    print(f'{name}님의 가입이 완료되었습니다.')


def member_all_get():
    global member_data

    print('---전체회원조회---')
    for i, mb in enumerate(member_data, 1):
        print(f'{i}. {mb['name']}')
    print(f'총 회원 : {len(member_data)}')

def member_get():
    global member_data

    name = input('조회할 회원의 이름을 입력해주세요 : ').strip()

    for mb in member_data:
        if mb['name'] == name:
            print(f'이름 : {mb['name']}')
            print(f'생일 : {mb['birth_date']}')
            print(f'가입일시 : {mb['register_date']}')
            break
    else:
        print('등록된 회원이 아닙니다.')


def member_update():
    global member_data

    print('---회원수정---')
    name = input('수정할 회원의 이름을 입력해주세요 : ')

    for mb in member_data:
        if mb['name'] == name:
            print('1. 이름 수정')
            print('2. 생일 수정')
            print('3. 비밀번호 수정')
            print('4. 뒤로가기')
            try:
                update_input = int(input('수정할 정보를 선택해주세요 : ').strip())
                if update_input==1:
                    old_name = mb['name']
                    new_name = input('변경할 이름을 입력해주세요 : ').strip()
                    mb['name'] = new_name
                    print(f'이름이 변경되었습니다 : {old_name} -> {new_name}')
                elif update_input == 2:
                    old_birth = mb['birth_date']
                    new_birth = date_input('변경할 생일을 입력해주세요')
                    mb['birth_date'] = new_birth
                    print(f'생일이 변경되었습니다 : {old_birth} -> {new_birth}')
                elif update_input == 3:
                    new_password = input('변경할 비밀번호를 입력해주세요 : ').strip()
                    mb['password'] = new_password
                    print(f'비밀번호가 변경되었습니다')
                elif update_input == 0:
                    member_update()
                elif update_input == 4:
                    break
                else:
                    print('메뉴 번호를 확인해주세요')
                    return 0
            except ValueError:
                print('번호를 입력해주세요')
                return 0
            break
    else:
        print('등록된 회원이 아닙니다.')


def member_delect():
    global member_data

    print('---회원삭제---')
    name = input('삭제할 회원의 이름을 입력해주세요 : ')

    for mb in member_data:
        if mb['name'] == name:
            rel_ck = input(f'{name}님을 정말로 삭제하시겠습니까? (y/n)').strip().lower()
            if rel_ck == 'y':
                member_data.remove(mb)
                print('회원이 삭제되었습니다')
            elif rel_ck == 'n':
                print('취소되었습니다')
            break
    else:
        print('등록된 회원이 아닙니다')

def member_save():
    global member_data

    print('---파일저장---')
    old_members = file_open()
    print(f'기존 회원 수 : {len(old_members)}')
    print(f'현재 회원 수 : {len(member_data)}')
    rel_ck = input('정말로 저장하시겠습니까? (y/n)').strip().lower()
    
    if rel_ck == 'y':
        file_save(member_data)
    elif rel_ck == 'n':
        print('저장이 취소되었습니다')
        

