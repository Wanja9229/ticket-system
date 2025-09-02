from typing import Optional, Union
from datetime import datetime

class Book:
    def __init__(self, title:str, author:str, isbn:str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available : bool = True
        self.borrowed_by : Optional[str] = None
        self.borrowed_date : Optional[datetime] = None

    def __str__(self):
        state = "대출 가능" if self.is_available else f"대출중"
        return f"[{self.isbn}] {self.title} - {self.author} | {state}"
    
class Member:
    def __init__(self, name:str, mb_id:str):
        self.name = name
        self.mb_id = mb_id
        self.borrowed_books = list
        self.max_books : int = 3
        self.join_date = int

    def __str__(self):
        return f"[{self.mb_id}] {self.name} | 대출: {len(self.borrowed_books)}/{self.max_books}"

    def can_borrow(self) -> bool:
            if len(self.borrowed_books) < self.max_books:
                return True
            else:
                return False
        
    def show_borrowed_books(self):
        if len(self.borrowed_books) > 0:
            print(f'{self.borrowed_books} / {self.max_books}')
        else:
            print('대출한 책이 없습니다.')

class Library:
    pass