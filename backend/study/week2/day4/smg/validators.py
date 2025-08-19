# validators.py - 데이터 검증 헬퍼
import datetime

class Validator:
    def validate_date(self, date_string: str) -> bool:
        """날짜 형식 검증 (YYYY-MM-DD)"""
        try:
            datetime.datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def validate_string_not_empty(self, value: str) -> bool:
        """문자열이 비어있지 않은지 검증"""
        return bool(value and value.strip())
    
    def validate_menu_choice(self, choice: str, max_choice: int) -> bool:
        """메뉴 선택 유효성 검증"""
        try:
            choice_num = int(choice)
            return 1 <= choice_num <= max_choice
        except ValueError:
            return False
    
    def validate_file_extension(self, filename: str, extension: str = '.json') -> bool:
        """파일 확장자 검증"""
        return filename.lower().endswith(extension.lower())
    
    def sanitize_filename(self, filename: str) -> str:
        """파일명 정리 (확장자 자동 추가)"""
        if not self.validate_file_extension(filename):
            filename += '.json'
        return filename