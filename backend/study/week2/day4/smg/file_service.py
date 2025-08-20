# file_service.py - 파일 입출력 관련 서비스
import json
import os
from typing import List, Dict, Optional

class FileService:
    def save_members_to_file(self, members: List[Dict[str, str]], filename: str) -> bool:
        """회원 정보를 JSON 파일로 저장"""
        try:   # 예외 처리 시작
            # 파일을 쓰기 모드로 열고, UTF-8 인코딩 사용
            with open(filename, 'w', encoding='utf-8') as f:
                # 회원 리스트를 JSON 형식으로 파일에 저장
                # ensure_ascii=False: 한글 등 유니코드 문자 그대로 저장
                # indent=4: JSON 형식을 보기 좋게 들여쓰기 4칸으로 정렬
                json.dump(members, f, ensure_ascii=False, indent=4)
            return True # 저장 성공 시 True 반환

        except PermissionError: # 파일 쓰기 권한이 없을 때 발생하는 예외
            print("파일에 쓰기 권한이 없습니다.") # 권한 오류 메시지 출력
            return False # 실패 시 False 반환
        except Exception as e: # 그 외 모든 예외 처리
            print(f"파일 저장 중 오류가 발생했습니다: {e}") # 일반적인 오류 메시지 출력
            return False # 실패 시 False 반환
    
    def load_members_from_file(self, filename: str) -> Optional[List[Dict[str, str]]]:
        """JSON 파일에서 회원 정보를 불러오기"""
        try: 
            # 파일을 읽기 모드로 열고, UTF-8 인코딩 사용
            with open(filename, 'r', encoding='utf-8') as f:
                # JSON 파일을 읽어서 Python 객체(리스트)로 변환
                members = json.load(f)
            return members # 성공적으로 읽은 회원 데이터 반환
            
        except FileNotFoundError:  # 파일이 존재하지 않을 때 발생하는 예외
            print(f"'{filename}' 파일을 찾을 수 없습니다.") # 파일 없음 오류 메시지
            return None # 실패 시 None 반환
        except json.JSONDecodeError:  # JSON 형식이 잘못되었을 때 발생하는 예외
            print("파일 형식이 올바르지 않습니다.")  # JSON 형식 오류 메시지
            return None # 실패 시 None 반환
        except Exception as e:  # 그 외 모든 예외 처리
            print(f"파일 읽기 중 오류가 발생했습니다: {e}") # 일반적인 오류 메시지 출력
            return None # 실패 시 None 반환
    
    def delete_file(self, filename: str) -> bool:
        """파일 삭제"""
        try:
            # 파일이 존재하지 않는지 확인
            if not os.path.exists(filename):
                print(f"'{filename}' 파일을 찾을 수 없습니다.") # 파일 없음 메시지
                return False  # 파일이 없으면 False 반환
            
            # 파일 삭제 실행
            os.remove(filename)
            return True # 삭제 성공 시 True 반환
            
        except PermissionError: # 파일 삭제 권한이 없을 때 발생하는 예외
            print("파일 삭제 권한이 없습니다.") # 권한 오류 메시지 출력
            return False # 실패 시 False 반환
        except Exception as e:  # 그 외 모든 예외 처리
            print(f"파일 삭제 중 오류가 발생했습니다: {e}")  # 일반적인 오류 메시지 출력
            return False # 실패 시 False 반환
    
    def file_exists(self, filename: str) -> bool:
        """파일 존재 여부 확인"""
        # os.path.exists()를 사용하여 파일 존재 여부를 확인하고 결과 반환
        # 파일이 존재하면 True, 없으면 False 반환
        return os.path.exists(filename)