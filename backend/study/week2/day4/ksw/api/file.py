import json
import os

def file_open() -> list[dict[str, str]]:
    if os.path.exists('data/members.json'):
        with open('data/members.json', 'r', encoding='utf-8') as mb:
            return json.load(mb)
    else:
        print('파일이 존재하지 않습니다')
        return []
    
    
def file_save(data: list[dict[str, str]]) -> bool:
    os.makedirs('data', exist_ok=True)

    try:
        with open('data/members.json', 'w', encoding='utf-8') as mb:
            json.dump(data, mb, ensure_ascii=False, indent=4)
        print('저장이 완료되었습니다')
        return True
    except Exception as error:
        print(f'저장이 실패했습니다 : {error}')
        return False