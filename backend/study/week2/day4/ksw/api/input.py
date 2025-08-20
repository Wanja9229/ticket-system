from datetime import datetime

def date_input(text: str) -> str:
    while True:
        date = input(f'{text} (YYYY-MM-DD) : ').strip()
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print('올바른 날짜 형식으로 입력해주세요. ')