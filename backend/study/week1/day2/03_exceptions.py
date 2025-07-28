"""
Week 1 - Day 2: 예외 처리

PHP의 try-catch와 Python의 try-except
"""

print("=== 1. 기본 예외 처리 ===")
# PHP:
# try {
#     $result = 10 / 0;
# } catch (Exception $e) {
#     echo "에러: " . $e->getMessage();
# }

try:
    result = 10 / 0
except ZeroDivisionError as e:  # PHP: catch (Exception $e)
    print(f"에러: {e}")

print("\n=== 2. 여러 예외 처리 ===")
def process_data(data):
    try:
        # 여러 종류의 에러가 발생할 수 있는 코드
        value = data["key"]
        number = int(value)
        result = 10 / number
        return result
    except KeyError:
        print("키를 찾을 수 없습니다")
    except ValueError:
        print("숫자로 변환할 수 없습니다")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
    except Exception as e:  # 모든 예외 포착 (PHP: catch (Exception $e))
        print(f"예상치 못한 에러: {e}")

# 테스트
print("테스트 1:")
process_data({"wrong_key": "10"})  # KeyError

print("\n테스트 2:")
process_data({"key": "abc"})  # ValueError

print("\n테스트 3:")
process_data({"key": "0"})  # ZeroDivisionError

print("\n=== 3. else와 finally ===")
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {filename}")
        return None
    else:
        # 예외가 발생하지 않았을 때만 실행
        print("파일을 성공적으로 읽었습니다")
        return content
    finally:
        # 예외 발생 여부와 관계없이 항상 실행
        # PHP: finally 블록과 동일
        try:
            file.close()
            print("파일을 닫았습니다")
        except:
            pass

# 테스트
print("존재하지 않는 파일:")
read_file("not_exist.txt")

print("\n=== 4. 예외 발생시키기 ===")
# PHP: throw new Exception("메시지");
# Python: raise Exception("메시지")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("나이는 정수여야 합니다")
    if age < 0:
        raise ValueError("나이는 0보다 커야 합니다")
    if age > 150:
        raise ValueError("나이가 너무 큽니다")
    return True

# 테스트
try:
    validate_age("스물")
except TypeError as e:
    print(f"타입 에러: {e}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"값 에러: {e}")

print("\n=== 5. 사용자 정의 예외 ===")
# PHP:
# class CustomException extends Exception {
#     public function __construct($message) {
#         parent::__construct($message);
#     }
# }

class ValidationError(Exception):
    """검증 실패 예외"""
    pass

class AuthenticationError(Exception):
    """인증 실패 예외"""
    def __init__(self, username):
        self.username = username
        super().__init__(f"인증 실패: {username}")

# 사용 예시
def login(username, password):
    if username != "admin":
        raise AuthenticationError(username)
    if password != "1234":
        raise ValidationError("잘못된 비밀번호입니다")
    return "로그인 성공"

try:
    result = login("user", "1234")
except AuthenticationError as e:
    print(f"인증 에러: {e}")
    print(f"실패한 사용자: {e.username}")
except ValidationError as e:
    print(f"검증 에러: {e}")

print("\n=== 6. 컨텍스트 매니저 (with 문) ===")
# PHP에는 없는 Python의 강력한 기능
# 자동으로 리소스를 정리해줍니다

# 파일 처리 (자동으로 close)
print("파일 처리 예시:")
try:
    with open("test.txt", "w") as f:
        f.write("Hello, Python!")
    # 여기서 파일이 자동으로 닫힙니다
    
    with open("test.txt", "r") as f:
        content = f.read()
        print(f"파일 내용: {content}")
except Exception as e:
    print(f"파일 처리 에러: {e}")

print("\n=== 7. 예외 체이닝 ===")
def process_user_data(user_id):
    try:
        # 데이터베이스에서 사용자 조회 시뮬레이션
        if user_id == 0:
            raise ValueError("잘못된 사용자 ID")
    except ValueError as e:
        # 원본 예외를 포함하여 새로운 예외 발생
        raise RuntimeError("사용자 처리 실패") from e

try:
    process_user_data(0)
except RuntimeError as e:
    print(f"런타임 에러: {e}")
    print(f"원인: {e.__cause__}")

print("\n=== 8. 예외 처리 모범 사례 ===")
def divide_numbers(a, b):
    """좋은 예외 처리 예시"""
    try:
        # 입력 검증
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("숫자만 입력 가능합니다")
        
        # 비즈니스 로직
        result = a / b
        
        # 결과 검증
        if result == float('inf'):
            raise OverflowError("결과가 너무 큽니다")
        
        return result
        
    except ZeroDivisionError:
        # 구체적인 에러 처리
        print("경고: 0으로 나누기 시도")
        return None
    except TypeError as e:
        # 로깅 (실제로는 로거 사용)
        print(f"타입 에러 로그: {e}")
        raise  # 재발생
    except Exception as e:
        # 예상치 못한 에러
        print(f"예상치 못한 에러: {type(e).__name__}: {e}")
        raise

# 테스트
print("정상 케이스:")
print(divide_numbers(10, 2))

print("\n0으로 나누기:")
print(divide_numbers(10, 0))

print("\n=== 주요 차이점 정리 ===")
print("""
PHP vs Python 예외 처리:
1. try-catch -> try-except
2. Exception $e -> Exception as e
3. throw -> raise
4. catch 대신 except 사용
5. else 블록 추가 (예외 없을 때)
6. with 문으로 자동 리소스 관리
7. 예외 체이닝 (from 키워드)
8. 더 세분화된 내장 예외 타입
""")

# 정리: 일반적인 Python 예외 타입들
print("\n=== 자주 사용하는 예외 타입 ===")
print("""
- ValueError: 잘못된 값
- TypeError: 잘못된 타입  
- KeyError: 딕셔너리 키 없음
- IndexError: 리스트 인덱스 범위 초과
- FileNotFoundError: 파일 없음
- ZeroDivisionError: 0으로 나누기
- AttributeError: 속성 없음
- ImportError: 모듈 임포트 실패
- RuntimeError: 런타임 에러
- Exception: 모든 예외의 기본 클래스
""")
