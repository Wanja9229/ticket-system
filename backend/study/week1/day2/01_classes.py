"""
Week 1 - Day 2: 클래스와 객체지향 프로그래밍

PHP와 Python의 클래스 비교
"""

print("=== 1. 기본 클래스 정의 ===")
# PHP:
# class User {
#     private $name;
#     private $age;
#     
#     public function __construct($name, $age) {
#         $this->name = $name;
#         $this->age = $age;
#     }
#     
#     public function getName() {
#         return $this->name;
#     }
# }

class User:
    def __init__(self, name, age):  # PHP: __construct
        self.name = name  # PHP: $this->name
        self.age = age
    
    def get_name(self):  # PHP: public function getName()
        return self.name
    
    def get_info(self):
        return f"{self.name} ({self.age}세)"

# 객체 생성
user = User("김철수", 25)  # PHP: $user = new User("김철수", 25);
print(f"이름: {user.get_name()}")
print(f"정보: {user.get_info()}")

print("\n=== 2. 프로퍼티와 메서드 ===")
class Product:
    # 클래스 변수 (PHP의 static 프로퍼티와 유사)
    tax_rate = 0.1  # PHP: private static $taxRate = 0.1;
    
    def __init__(self, name, price):
        # 인스턴스 변수
        self.name = name
        self.price = price
        self._discount = 0  # _ 접두사: 내부용 (관례)
        self.__secret = "비밀"  # __ 접두사: private (name mangling)
    
    def set_discount(self, discount):
        if 0 <= discount <= 100:
            self._discount = discount
    
    def get_final_price(self):
        discounted = self.price * (1 - self._discount / 100)
        return discounted * (1 + self.tax_rate)

product = Product("노트북", 1000000)
product.set_discount(10)
print(f"최종 가격: {product.get_final_price():,.0f}원")

print("\n=== 3. 상속 ===")
# PHP:
# class Employee extends User {
#     private $salary;
#     
#     public function __construct($name, $age, $salary) {
#         parent::__construct($name, $age);
#         $this->salary = $salary;
#     }
# }

class Employee(User):  # User 클래스 상속
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # PHP: parent::__construct()
        self.salary = salary
    
    def get_info(self):  # 메서드 오버라이딩
        return f"{super().get_info()}, 급여: {self.salary:,}원"

emp = Employee("박지민", 30, 3000000)
print(f"직원 정보: {emp.get_info()}")

print("\n=== 4. 클래스 메서드와 정적 메서드 ===")
class Calculator:
    # 정적 메서드 (PHP: public static function)
    @staticmethod
    def add(a, b):
        return a + b
    
    # 클래스 메서드
    @classmethod
    def create_with_default(cls):
        return cls()  # 자기 자신의 인스턴스 생성

# 정적 메서드는 인스턴스 없이 호출
result = Calculator.add(5, 3)  # PHP: Calculator::add(5, 3)
print(f"5 + 3 = {result}")

print("\n=== 5. 프로퍼티 데코레이터 (getter/setter) ===")
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property  # getter
    def celsius(self):
        return self._celsius
    
    @celsius.setter  # setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("절대영도보다 낮을 수 없습니다")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature()
temp.celsius = 25  # setter 호출
print(f"섭씨: {temp.celsius}°C")  # getter 호출
print(f"화씨: {temp.fahrenheit}°F")

print("\n=== 6. 매직 메서드 (특수 메서드) ===")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):  # PHP: __toString()
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):  # 개발자용 문자열 표현
        return f"Book('{self.title}', '{self.author}')"
    
    def __eq__(self, other):  # 동등 비교
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book("Python 입문", "김작가")
book2 = Book("Python 입문", "김작가")
print(str(book1))  # __str__ 호출
print(book1 == book2)  # __eq__ 호출

print("\n=== 주요 차이점 정리 ===")
print("""
PHP vs Python 클래스:
1. class 키워드는 동일, extends -> 괄호 사용
2. $this -> self (self는 첫 번째 매개변수로 명시)
3. __construct -> __init__
4. private/public 키워드 없음 (관례: _내부용, __private)
5. parent:: -> super()
6. :: -> . (정적 메서드도 . 사용)
7. new 키워드 없음
8. @property로 getter/setter 구현
""")
