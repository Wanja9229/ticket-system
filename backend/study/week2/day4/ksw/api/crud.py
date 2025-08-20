import json
import os
from datetime import datetime

from api.input import *

members_data = []

def member_old():
    global members_data
    if not os.path.exists('data/members.json'):
        members_data = []
    else:
        with open('data/members.json', 'r', encoding='utf-8') as mb:
            members_data = json.load(mb)

def member_input():
    global members_data

    print('======회원가입======')
    name = input('이름을 입력해주세요 : ').strip()
    birth = date_input('생일을 입력해주세요 : ')
    password = input('비밀번호를 입력해주세요 : ').strip()
    register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    new_member={
        'name':name,
        'birth_date':birth,
        'password':password,
        'register_date':register_date,
    }

    members_data.append(new_member)

    print(f'======{name} 님의 가입이 {register_date} 에 완료되었습니다======')
    print(f'======현재 총 회원 수 : {len(members_data)} 명======')
    print(f'======※변경 사항은 저장을 실행해야 반영됩니다======')


def member_list_get():
    global members_data
    print('======전체 회원 목록======')
    for i, member in enumerate(members_data, 1):
        print(f"{i}. {member['name']}")


def member_get():
    global members_data

    print('======회원 조회======')
    name = input('조회할 이름을 입력해주세요 : ')

    for member in members_data:
        if member['name'] == name:
            print(f"이름 : {member['name']}")
            print(f"생일 : {member['birth_date']}")
            print(f"가입일 : {member['register_date']}")
            break
    else:
        print(f'{name} 님은 존재하지 않는 회원입니다.')


def member_update():
    global members_data

    print('======회원 수정======')
    name = input('수정할 회원의 이름을 입력하세요 : ')
    for member in members_data:
        if member['name'] == name:
            print(f"1. 이름 : {member['name']}")
            print(f"2. 생일 : {member['birth_date']}")
            print(f"3. 비밀번호 : {'*'*len(member['password'])}")
            print("수정할 항목을 선택하세요 : ")
            
            while True:
                try:
                    choice = int(input('수정 항목 : '))
                    if 1 <= choice <= 3:
                        break
                    else:
                        print('메뉴 정보를 확인해주세요.')
                except ValueError:
                    print('실행할 메뉴의 숫자를 입력해 주세요.')

            if choice == '1':
                old_name = member['name']
                new_name = input("새 이름 : ").strip()
                member['name'] = new_name
                print(f'{old_name} 님의 이름이 {new_name} 으로 변경되었습니다.')
            elif choice == '2':
                new_birth = date_input('새 생일')
                member['birth_date'] = new_birth
                print(f'{member['name']} 님의 생일이 {new_birth} 으로 변경되었습니다.')
            elif choice == '3':
                new_password = input('새 비밀번호를 입력해주세요 : ')
                member['password'] = new_password
                print(f'{member['name']} 님의 비밀번호가 변경되었습니다.')
            break
    else:
        print(f'{name} 님은 존재하지 않는 회원입니다.')


def member_delete():
    print('회원삭제')


def file_save():
    print('파일저장')
