## file_service.py
### import 내용
import json
import os
from typing import List, Dict, Optional

### FileService 클래스
class FileService():
    # 회원 정보를 JSON 파일로 저장
    def save_members_to_file(self, members: List[Dict[str, str]], filename: str) -> bool:
        try:
            with open(filename, "w", encoding='utf-8') as f:
                json.dump(members, f, ensure_ascii=False, indent=4)
            return True
        except PermissionError:
            print("파일 쓰기 권한이 없습니다.")
            return False
        except Exception as e:
            print(f"파일 저장 중 오류가 발생했습니다: {e}")
            return False
        
    # JSON 파일에서 회원 정보 불러오기
    def load_members_from_file(self, filename: str) -> Optional[List[Dict[str, str]]]:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                member_data = json.load(f)
            return member_data
        except FileNotFoundError:
            print(f"{filename} 파일을 찾을 수 없습니다.")
            return None
        except json.JSONDecodeError:
            print("파일형식이 올바르지 않습니다.")
            return None
        except Exception as e:
            print(f"파일 읽기 중 오류가 발생했습니다: {e}")
            return None
        
    # 파일 삭제
    def delete_file(self, filename: str) -> bool:
        try:
            if not os.path.exists(filename):
                print(f"'{filename}' 파일을 찾을 수 없습니다.")
                return False
            os.remove(filename)
            return True
        except PermissionError:
            print("파일 삭제 권한이 없습니다.")
            return False
        except Exception as e:
            print(f"파일 삭제 중 오류가 발생했습니다: {e}")
            return False