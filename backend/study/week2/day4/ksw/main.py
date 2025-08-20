from api.menu import menu_pop, menu_choice
from api.crud import *


def main():
    menu_dict = {
        1 : member_input,
        2 : member_list_get,
        3 : member_get,
        4 : member_update,
        5 : member_delete,
        6 : member_save
    }
    while True:
        menu_pop()
        menu_num = menu_choice()

        if menu_num == 0:
            continue
        elif menu_num == 7:
            # 종료
            print('------프로그램을 종료합니다------')
            break
        elif menu_num in menu_dict:
            menu_dict[menu_num]()

main()