"""
file_handler.py - 파일 입출력 처리 모듈
JSON 파일을 읽고 쓰는 기능을 담당하는 모듈입니다.
파일 존재 여부 확인, 백업 생성 등의 기능도 포함합니다.
"""

# 필요한 모듈들을 가져옵니다
import json  # JSON 파일을 다루기 위한 모듈
import os  # 파일 시스템 관련 작업을 위한 모듈
from typing import List, Dict  # 타입 힌트를 위한 모듈
# shutil과 datetime import 제거 (백업 기능 제거로 불필요)


def load_from_file(filename: str) -> List[Dict[str, str]]:
    """
    JSON 파일에서 회원 데이터를 읽어오는 함수입니다.
    
    매개변수:
        filename: 읽을 파일의 이름
    
    반환값: List[Dict[str, str]] - 회원 정보 딕셔너리들의 리스트
            파일이 없거나 오류가 발생하면 빈 리스트 반환
    """
    # 파일명에 .json 확장자가 없으면 추가
    if not filename.endswith('.json'):
        filename += '.json'
    
    try:
        # with문을 사용하면 파일이 자동으로 닫힙니다
        # 'r'은 읽기 모드, encoding='utf-8'은 한글 지원
        with open(filename, 'r', encoding='utf-8') as file:
            # json.load()로 파일 내용을 파이썬 객체로 변환
            members = json.load(file)
            print(f"✅ {filename} 파일에서 {len(members)}명의 회원 정보를 불러왔습니다.")
            return members
            
    except FileNotFoundError:
        # 파일이 존재하지 않는 경우
        print(f"❌ {filename} 파일을 찾을 수 없습니다.")
        return []
        
    except json.JSONDecodeError:
        # JSON 형식이 올바르지 않은 경우
        print(f"❌ {filename} 파일의 형식이 올바르지 않습니다.")
        return []
        
    except PermissionError:
        # 파일 접근 권한이 없는 경우
        print(f"❌ {filename} 파일에 접근할 수 없습니다. 권한을 확인해주세요.")
        return []
        
    except Exception as e:
        # 기타 예상치 못한 오류
        print(f"❌ 파일을 읽는 중 오류가 발생했습니다: {str(e)}")
        return []


def save_to_file(members: List[Dict[str, str]], filename: str) -> bool:
    """
    회원 데이터를 JSON 파일로 저장하는 함수입니다.
    
    매개변수:
        members: 저장할 회원 정보 리스트
        filename: 저장할 파일의 이름
    
    반환값: bool - 저장 성공시 True, 실패시 False
    """
    # 파일명에 .json 확장자가 없으면 추가
    if not filename.endswith('.json'):
        filename += '.json'
    
    try:
        # 백업 생성 코드 제거 - 바로 파일 저장
        # with문을 사용하여 파일 자동 닫기
        # 'w'는 쓰기 모드 (기존 내용을 덮어씀)
        with open(filename, 'w', encoding='utf-8') as file:
            # json.dump()로 파이썬 객체를 JSON 형식으로 파일에 저장
            # ensure_ascii=False: 한글이 유니코드로 변환되지 않게 함
            # indent=4: 들여쓰기 4칸으로 보기 좋게 저장
            json.dump(members, file, ensure_ascii=False, indent=4)
            
        print(f"✅ {len(members)}명의 회원 정보가 {filename} 파일에 저장되었습니다.")
        return True
        
    except PermissionError:
        # 파일 쓰기 권한이 없는 경우
        print(f"❌ {filename} 파일에 쓸 수 없습니다. 권한을 확인해주세요.")
        return False
        
    except Exception as e:
        # 기타 예상치 못한 오류
        print(f"❌ 파일 저장 중 오류가 발생했습니다: {str(e)}")
        return False


def delete_file(filename: str) -> bool:
    """
    파일을 삭제하는 함수입니다.
    
    매개변수:
        filename: 삭제할 파일의 이름
    
    반환값: bool - 삭제 성공시 True, 실패시 False
    """
    # 파일명에 .json 확장자가 없으면 추가
    if not filename.endswith('.json'):
        filename += '.json'
    
    try:
        # 파일이 존재하는지 먼저 확인
        if not os.path.exists(filename):
            print(f"❌ {filename} 파일이 존재하지 않습니다.")
            return False
        
        # os.remove()로 파일 삭제
        os.remove(filename)
        print(f"✅ {filename} 파일이 삭제되었습니다.")
        return True
        
    except PermissionError:
        # 파일 삭제 권한이 없는 경우
        print(f"❌ {filename} 파일을 삭제할 수 없습니다. 권한을 확인해주세요.")
        return False
        
    except Exception as e:
        # 기타 예상치 못한 오류
        print(f"❌ 파일 삭제 중 오류가 발생했습니다: {str(e)}")
        return False


def check_file_exists(filename: str) -> bool:
    """
    파일이 존재하는지 확인하는 함수입니다.
    
    매개변수:
        filename: 확인할 파일의 이름
    
    반환값: bool - 존재하면 True, 없으면 False
    """
    # 파일명에 .json 확장자가 없으면 추가
    if not filename.endswith('.json'):
        filename += '.json'
    
    # os.path.exists()로 파일 존재 여부 확인
    return os.path.exists(filename)