# validators.py - 데이터 검증 헬퍼
from datetime import datetime

class Validator:
    def validate_date(self, date_string: str) -> bool:
        """날짜 형식 검증 (YYYY-MM-DD)"""
        try:
            # 입력받은 문자열을 YYYY-MM-DD 형식으로 파싱 시도
            # strptime: 문자열을 지정된 형식의 datetime 객체로 변환
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def validate_string_not_empty(self, value: str) -> bool:
        """문자열이 비어있지 않은지 검증"""
        # value가 존재하고(None이 아니고) 공백을 제거한 후에도 내용이 있는지 확인
        # value.strip(): 문자열 앞뒤 공백 제거
        # bool(): 결과를 True/False로 변환 (빈 문자열은 False, 내용이 있으면 True)
        return bool(value and value.strip())
     
    def validate_file_extension(self, filename: str, extension: str = '.json') -> bool:
        """파일 확장자 검증"""
        # filename을 소문자로 변환하고 지정된 확장자로 끝나는지 확인
        # extension도 소문자로 변환하여 대소문자 구분 없이 비교
        # endswith(): 문자열이 특정 문자열로 끝나는지 확인하는 메서드
        return filename.lower().endswith(extension.lower())
    
    def sanitize_filename(self, filename: str) -> str:
        """파일명 정리 (확장자 자동 추가)"""
        # 파일명이 올바른 확장자를 가지고 있지 않은지 확인
        if not self.validate_file_extension(filename):
            # 확장자가 없으면 .json 확장자를 자동으로 추가
            filename += '.json'
        # 정리된 파일명 반환 (확장자가 있으면 그대로, 없으면 .json 추가된 상태)
        return filename