# member_manager.py - 회원 관리 메인 클래스
from typing import List, Dict
from member_service import MemberService
from file_service import FileService
from ui_helper import UIHelper
from validators import Validator

class MemberManager:
    def __init__(self):
        # 메모리상에 임시 저장할 회원 정보 리스트
        self.members: List[Dict[str, str]] = []
        
        # 서비스 클래스들 초기화
        self.member_service = MemberService()
        self.file_service = FileService()
        self.ui_helper = UIHelper()
        self.validator = Validator()
    
    def register_member(self) -> None:
        """회원가입 기능"""
        print("\n=== 회원가입 ===")
        
        try:
            # 회원 정보 입력 받기
            member_data = self.ui_helper.get_member_input()
            
            if member_data:
                # 회원 생성
                member = self.member_service.create_member(member_data)
                self.members.append(member)
                print(f"회원 '{member['name']}'이 성공적으로 등록되었습니다.")
            
        except Exception as e:
            print(f"회원가입 중 오류가 발생했습니다: {e}")
    
    def save_to_file(self) -> None:
        """파일 저장 기능"""
        print("\n=== 파일 저장 ===")
        
        if not self.members:
            print("저장할 회원 정보가 없습니다.")
            return
        
        filename = self.ui_helper.get_filename_input("저장할 파일명을 입력하세요")
        success = self.file_service.save_members_to_file(self.members, filename)
        
        if success:
            print(f"총 {len(self.members)}명의 회원 정보가 '{filename}' 파일에 저장되었습니다.")
    
    def search_member(self) -> None:
        """회원 정보 조회 기능"""
        print("\n=== 회원 정보 조회 ===")
        
        filename = self.ui_helper.get_filename_input("조회할 파일명을 입력하세요")
        member_name = input("조회할 회원 이름을 입력하세요: ").strip()
        
        members = self.file_service.load_members_from_file(filename)
        if members is not None:
            member = self.member_service.find_member_by_name(members, member_name)
            if member:
                self.ui_helper.display_member_info(member)
            else:
                print(f"'{member_name}' 회원을 찾을 수 없습니다.")
    
    def list_all_members(self) -> None:
        """전체 회원 목록 조회 기능"""
        print("\n=== 전체 회원 목록 ===")
        
        filename = self.ui_helper.get_filename_input("조회할 파일명을 입력하세요")
        members = self.file_service.load_members_from_file(filename)
        
        if members is not None:
            if members:
                self.ui_helper.display_members_list(members)
            else:
                print("등록된 회원이 없습니다.")
    
    def update_member(self) -> None:
        """회원 정보 수정 기능"""
        print("\n=== 회원 정보 수정 ===")
        
        filename = self.ui_helper.get_filename_input("수정할 파일명을 입력하세요")
        member_name = input("수정할 회원 이름을 입력하세요: ").strip()
        
        members = self.file_service.load_members_from_file(filename)
        if members is None:
            return
        
        # 수정할 회원 찾기
        member_index, error = self.member_service.find_member_for_update(members, member_name)
        if error:
            print(error)
            return
        
        # 현재 회원 정보 출력
        current_member = members[member_index]
        self.ui_helper.display_current_member_info(current_member)
        
        # 수정할 항목 선택
        choice = self.ui_helper.get_update_choice()
        
        success = False
        message = ""
        
        if choice == '1':
            new_birth_date = self.ui_helper.get_new_birth_date()
            success, message = self.member_service.update_birth_date(members, member_index, new_birth_date)
        elif choice == '2':
            new_password = self.ui_helper.get_new_password()
            success, message = self.member_service.update_password(members, member_index, new_password)
        else:
            print("잘못된 선택입니다.")
            return
        
        print(message)
        
        if success:
            file_success = self.file_service.save_members_to_file(members, filename)
            if file_success:
                print("회원 정보가 성공적으로 수정되고 저장되었습니다.")
            else:
                print("파일 저장에 실패했습니다.")
    
    def delete_file(self) -> None:
        """파일 삭제 기능"""
        print("\n=== 파일 삭제 ===")
        
        filename = self.ui_helper.get_filename_input("삭제할 파일명을 입력하세요")
        confirm = self.ui_helper.get_delete_confirmation(filename)
        
        if confirm:
            success = self.file_service.delete_file(filename)
            if success:
                print(f"'{filename}' 파일이 성공적으로 삭제되었습니다.")
        else:
            print("파일 삭제가 취소되었습니다.")
    
    def run(self) -> None:
        """메인 실행 함수"""
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
    
    def run(self) -> None:
        """메인 실행 함수"""
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