

from api.menu import menu_input, menu_pop
from api.crud import *

member_data = []

def main():
    menu_dict = {
        1 : member_input,
        2 : member_all_get,
        3 : member_get,
        4 : member_update,
        5 : member_delect,
        6 : member_save
    }
    
    while True:
        menu_pop()
        menu_num = int(menu_input())
        if 1 <= menu_num <= 6:
            menu_dict[menu_num]()
        elif menu_num == 0:
            continue
        elif menu_num == 7:
            print('저장하지 않은 사항은 반영되지 않습니다')
            rel_ck = input('정말로 종료하시겠습니까? (y / n) : ').strip()
            if rel_ck == 'y':
                break
            elif rel_ck == 'n':
                continue

main()