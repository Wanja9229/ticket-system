# member_service.py - 회원 관련 비즈니스 로직
import datetime
from typing import List, Dict, Optional
from validators import Validator

class MemberService:
    def __init__(self):
        self.validator = Validator()
    
    def create_member(self, member_data: Dict[str, str]) -> Dict[str, str]:
        """회원 정보 딕셔너리 생성"""
        register_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        member = {
            "name": member_data["name"],
            "birth_date": member_data["birth_date"],
            "register_date": register_date,
            "password": member_data["password"]
        }
        
        return member
    
    def find_member_by_name(self, members: List[Dict[str, str]], name: str) -> Optional[Dict[str, str]]:
        """이름으로 회원 찾기"""
        for member in members:
            if member['name'] == name:
                return member
        return None
    
    def find_member_index_by_name(self, members: List[Dict[str, str]], name: str) -> int:
        """이름으로 회원 인덱스 찾기"""
        for i, member in enumerate(members):
            if member['name'] == name:
                return i
        return -1
    
    def find_member_for_update(self, members: List[Dict[str, str]], member_name: str) -> tuple[int, Optional[str]]:
        """수정할 회원 찾기 - 인덱스와 에러 메시지 반환"""
        member_index = self.find_member_index_by_name(members, member_name)
        
        if member_index == -1:
            return -1, f"'{member_name}' 회원을 찾을 수 없습니다."
        
        return member_index, None
    
    def update_birth_date(self, members: List[Dict[str, str]], member_index: int, new_birth_date: str) -> tuple[bool, str]:
        """생년월일 수정"""
        if not self.validator.validate_date(new_birth_date):
            return False, "생년월일 형식이 올바르지 않습니다."
        
        members[member_index]['birth_date'] = new_birth_date
        return True, "생년월일이 수정되었습니다."
    
    def update_password(self, members: List[Dict[str, str]], member_index: int, new_password: str) -> tuple[bool, str]:
        """패스워드 수정"""
        if not new_password.strip():
            return False, "패스워드는 필수 입력 항목입니다."
        
        members[member_index]['password'] = new_password
        return True, "패스워드가 수정되었습니다."