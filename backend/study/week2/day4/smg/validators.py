## validators.py
### import 내용
from datetime import datetime

### Validator 클래스
class Validator():
    # 날짜 형식 검증 (YYYY-MM-DD) => try:
    def validate_date(self, date_string: str) -> bool:
        try:
            datetime.strptime(date_string, "%Y-%M-%d")
            return True
        except ValueError:
            return False

    # 문자열이 비어있지 않은지 검증
    def validate_string_not_empty(self, value: str) -> bool:
        return bool(value and value.strip())

    # 파일 확장자 검증
    def validate_file_extension(self, filename: str, extension: str = '.json') -> bool:
        return filename.lower().endswith(extension.lower())

    # 파일명 정리 (확장자 자동 추가)
    def sanitize_filename(self, filename: str) -> str:
        if not self.validate_file_extension(filename):
            filename += ".json"
        return filename