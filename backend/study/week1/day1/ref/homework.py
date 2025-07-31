"""
Week 1 - Day 1 과제

PHP 코드를 Python으로 변환하고, Python 스타일로 개선하기
"""

# 과제 1: PHP 함수를 Python으로 변환하기
# 다음 PHP 코드를 Python으로 변환하세요:
"""
PHP 코드:
function calculateTotal($items) {
    $total = 0;
    foreach ($items as $item) {
        if ($item['quantity'] > 0) {
            $total += $item['price'] * $item['quantity'];
        }
    }
    return $total;
}
"""

# 여기에 Python 코드 작성:
def calculate_total(items):
    # TODO: 구현하세요
    pass


# 과제 2: 사용자 검증 함수 만들기
# 다음 조건을 만족하는 validate_user 함수를 작성하세요:
# - 이름은 2자 이상
# - 나이는 18세 이상 100세 이하
# - 이메일에는 @가 포함되어야 함
# - 모든 조건을 만족하면 True, 아니면 False 반환

def validate_user(name, age, email):
    # TODO: 구현하세요
    pass


# 과제 3: 리스트 처리
# numbers 리스트에서:
# 1. 짝수만 필터링
# 2. 각 숫자를 제곱
# 3. 결과를 리스트로 반환

def process_numbers(numbers):
    # TODO: 구현하세요
    # 힌트: List Comprehension 사용해보세요
    pass


# 과제 4: 딕셔너리 다루기
# 학생 정보를 담은 딕셔너리 리스트에서
# 평균 점수가 80점 이상인 학생의 이름만 리스트로 반환

def get_honor_students(students):
    """
    students 예시:
    [
        {"name": "김철수", "score": 85},
        {"name": "이영희", "score": 75},
        {"name": "박민수", "score": 90}
    ]
    """
    # TODO: 구현하세요
    pass


# 테스트 코드 (수정하지 마세요)
if __name__ == "__main__":
    # 과제 1 테스트
    items = [
        {"name": "사과", "price": 1000, "quantity": 3},
        {"name": "바나나", "price": 500, "quantity": 0},
        {"name": "오렌지", "price": 1500, "quantity": 2}
    ]
    print(f"과제 1 - 총액: {calculate_total(items)}")  # 예상: 6000
    
    # 과제 2 테스트
    print(f"과제 2 - 유효한 사용자: {validate_user('홍길동', 25, 'hong@email.com')}")  # True
    print(f"과제 2 - 짧은 이름: {validate_user('김', 25, 'kim@email.com')}")  # False
    
    # 과제 3 테스트
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"과제 3 - 짝수 제곱: {process_numbers(numbers)}")  # [4, 16, 36, 64, 100]
    
    # 과제 4 테스트
    students = [
        {"name": "김철수", "score": 85},
        {"name": "이영희", "score": 75},
        {"name": "박민수", "score": 90},
        {"name": "최지우", "score": 82}
    ]
    print(f"과제 4 - 우등생: {get_honor_students(students)}")  # ['김철수', '박민수', '최지우']


# 보너스 과제: PHP의 array_map과 같은 동작을 하는 함수 만들기
def array_map(func, array):
    """
    PHP: array_map(function($x) { return $x * 2; }, $array);
    Python: array_map(lambda x: x * 2, array)
    """
    # TODO: 구현하세요
    pass
