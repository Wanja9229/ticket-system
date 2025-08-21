import json
import os

def file_open() -> list[dict[str: str]]:
    with open('data/members.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def file_save(data: list[dict[str: str]]) -> bool:
    os.makedirs('data', exist_ok=True)

    try:
        with open('data/members.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print('성공적으로 저장되었습니다')
        return True
    except Exception as error:
        print(f'저장이 실패했습니다 : ({error})')
        return False