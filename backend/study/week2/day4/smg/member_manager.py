## member_manager.py
### import 내용
from typing import List, Dict
from member_service import MemberService
from file_service import FileService
from ui_helper import UIHelper
from validators import Validator

### MemberManager 클래스
# 생성자, 서비스 클래스들 초기화
class MemberManager():

    def __init__(self):
        self.members: List[Dict[str, str]] = []

        self.member_service = MemberService()
        self.file_service = FileService()
        self.ui_helper = UIHelper()
        self.validator = Validator()

    # 회원가입 기능 ** >> try
    def register_member(self) -> None:
        print("\n===회원 가입===")

        try:
            #회원 정보 입력받기
            member_data = self.ui_helper.get_member_input()
            if member_data:
                #회원 정보 딕셔너리에 넣기
                member = self.member_service.create_member(member_data)
                #회원 정보 메모리에 넣기
                self.members.append(member)
                print(f"회원 '{member['name']}' 이 성공적으로 등록되었습니다.")
        except Exception as e:
            print(f"회원가입 중 오류가 발생했습니다: {e}")

            
    # 파일 저장 기능
    def save_to_file(self) -> None: 
        print("\n===파일 저장===")

        if not self.members:
            print("저장할 회원 정보가 없습니다.")
            return

        #저장할 파일 이름 받기
        filename = self.ui_helper.get_filename_input("저장하실 파일명을 입력해주세요")

        #입력받은 이름으로 파일 생성
        success = self.file_service.save_members_to_file(self.members, filename)
        if success:
            print(f"\n 총 {len(self.members)}명의 회원 정보가 '{filename}' 파일에 저장 완료 되었습니다.")
     

    # 회원 정보 조회 기능
    def search_member(self) -> None:
        print("\n===회원 정보 조회===")

        #조회할 회원 파일 이름 받기
        filename = self.ui_helper.get_filename_input("조회하실 파일명을 입력해주세요")
        #조회할 회원 이름 받기
        member_name = input("조회할 회원 이름을 입력해주세요: ").strip()

        #받은 회원 파일 읽기
        members_data = self.file_service.load_members_from_file(filename)

        if members_data is not None:
            # 이름으로 해당 회원 조회하기
            member_data = self.member_service.find_member_by_name(members_data, member_name)
            if member_data:
                #회원 정보 보여주기
                self.ui_helper.display_member_info(member_data)
            else:
                print(f"'{member_name}' 회원을 찾을 수 없습니다.")

    # 전체 회원 목록 조회 기능
    def list_all_members(self) -> None:
        print("\n===전체 회원 목록===")

        #조회할 회원 파일 이름 받기
        filename = self.ui_helper.get_filename_input("조회하실 파일명을 입력해주세요.")

        #해당 파일에 있는 모든 회원 정보 읽어어서 보여주기
        #받은 회원 파일 읽기
        members_data = self.file_service.load_members_from_file(filename)

        if members_data is not None:
            if members_data:
                # 이름으로 해당 회원 조회하기
                self.ui_helper.display_members_list(members_data)
            else:
                print("조회할 회원이 없습니다.")
           
    # 회원 정보 수정 기능
    def update_member(self) -> None:
        print("\n===회원 정보 수정===")

        #조회할 회원 파일 이름 받기
        filename = self.ui_helper.get_filename_input("수정할 파일명을 입력해주세요.")

        #조회할 회원 이름 받기
        member_name = input("수정할 회원 이름을 입력해주세요: ").strip()

        #받은 회원 파일 읽기
        members_data = self.file_service.load_members_from_file(filename)

        if members_data is None:
            return
        
        memberindx, error = self.member_service.find_member_for_update(members_data, member_name)

        if error:
            print(error)
            return
        
        #수정할 회원의 기존 정보
        current_member = members_data[memberindx]
        
        #수정할 회원의 기존 정보 보여주기
        self.ui_helper.display_member_info(current_member)

        #수정할 항목 선택 
        choice_num = self.ui_helper.get_update_choice()

        mgs = ''
        if choice_num == '1':
            #새로운 생년월일 받음
            new_birth_date = self.ui_helper.get_new_birth_date()
            #새로운 생년월일로 update
            success_result, mgs = self.member_service.update_birth_date(members_data, memberindx, new_birth_date)
        elif choice_num == '2':
            #새로운 패스워드 받음
            new_password = self.ui_helper.get_new_password()
            #새로운 패스워드로 update
            success_result, mgs = self.member_service.update_password(members_data, memberindx, new_password)
        else:
            print("잘못된 선택입니다.")
            return
        
        print(mgs)

        
        if success_result: #새로운 정보가 잘 업데이트 되었다면 저장하기
            save_flag = self.file_service.save_members_to_file(members_data, filename)
            if save_flag:
                print("회원정보가 성공적으로 수정되고 저장되었습니다.")
            else:
                print("파일 저장에 실패했습니다.")

    # 파일 삭제 기능
    def delete_file(self) -> None:
        print("\n===파일 삭제===")

        # 삭제할 파일 명 받기
        filename = self.ui_helper.get_filename_input("삭제하실 파일명을 입력해주세요.")

        # 파일 삭제할 건 지 확인
        delete_flag = self.ui_helper.get_delete_confirmation(filename)

        if delete_flag:
            # 파일 처리
            del_sucess = self.file_service.delete_file(filename) 
            if del_sucess:
                print(f"'{filename}' 파일을 삭제가 완료되었습니다.")
        else:
            print("파일 삭제가 취소되었습니다.")

    # 메인 실행 함수
    def run(self) -> None:
        while True:
            self.ui_helper.show_menu()
            choice = input("메뉴를 선택하세요 (1-7): ").strip()
            
            if choice == '1':
                self.register_member()
            elif choice == '2':
                self.save_to_file()
            elif choice == '3':
                self.search_member()
            elif choice == '4':
                self.list_all_members()
            elif choice == '5':
                self.update_member()
            elif choice == '6':
                self.delete_file()
            elif choice == '7':
                print("프로그램을 종료합니다. 감사합니다!")
                break
            else:
                print("잘못된 선택입니다. 1-7 사이의 숫자를 입력해주세요.")
            
            input("\n계속하려면 Enter 키를 누르세요...")