# file_service.py - 파일 입출력 관련 서비스
import json
import os
from typing import List, Dict, Optional

class FileService:
    def save_members_to_file(self, members: List[Dict[str, str]], filename: str) -> bool:
        """회원 정보를 JSON 파일로 저장"""

        # 특정 폴더 지정 (예: data 폴더)
        save_path = os.path.join("data", filename)
        
        # data 폴더가 없으면 생성
        os.makedirs("data", exist_ok=True)
        
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(members, f, ensure_ascii=False, indent=4)
            return True

        except PermissionError:
            print("파일에 쓰기 권한이 없습니다.")
            return False
        except Exception as e:
            print(f"파일 저장 중 오류가 발생했습니다: {e}")
            return False
    
    def load_members_from_file(self, filename: str) -> Optional[List[Dict[str, str]]]:
        """JSON 파일에서 회원 정보를 불러오기"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                members = json.load(f)
            return members
            
        except FileNotFoundError:
            print(f"'{filename}' 파일을 찾을 수 없습니다.")
            return None
        except json.JSONDecodeError:
            print("파일 형식이 올바르지 않습니다.")
            return None
        except Exception as e:
            print(f"파일 읽기 중 오류가 발생했습니다: {e}")
            return None
    
    def delete_file(self, filename: str) -> bool:
        """파일 삭제"""
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
    
    def file_exists(self, filename: str) -> bool:
        """파일 존재 여부 확인"""
        return os.path.exists(filename)