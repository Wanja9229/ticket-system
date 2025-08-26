# 🎮 게임 캐릭터 시스템 - 7회차 학습 자료 (전투 시스템 포함)

## 📚 학습 목표
- 클래스 상속과 오버라이딩 완전 이해
- CRUD (Create, Read, Update, Delete) 구현
- 정적 메서드와 인스턴스 메서드 차이점
- 다형성과 isinstance() 활용
- **실전 전투 시스템을 통한 메서드 활용**

---

## 🏗️ 프로젝트 구조

### 📂 클래스 설계
```
Character (부모 클래스)
├── Warrior (전사) - 상속
├── Mage (마법사) - 상속
└── Archer (궁수) - 상속

CharacterManager (관리 클래스) - 정적 메서드들
```

---

## 🔥 핵심 개념들

### 1. **상속 (Inheritance)**
```python
class Character:        # 부모 클래스
    def attack(self):
        return "기본 공격!"

class Warrior(Character):  # 자식 클래스 - Character 상속받음
    def __init__(self, name):
        super().__init__(name, hp=150, mp=30)  # 부모 생성자 호출
```

**포인트:**
- `class Warrior(Character):` - 상속 문법
- `super().__init__()` - 부모 클래스 초기화 호출
- 부모의 모든 메서드와 속성을 자동으로 물려받음

### 2. **오버라이딩 (Method Overriding)**
```python
# 부모 클래스
def attack(self):
    return f"{self.name}이(가) 기본 공격!"

# 자식 클래스에서 재정의
def attack(self):
    damage = self.strength + 10
    return f"{self.name}이(가) 칼로 강력하게 공격! (데미지: {damage})"
```

**포인트:**
- 부모 메서드와 같은 이름으로 정의하면 덮어씀
- 각 클래스마다 다른 동작 구현 가능

### 3. **클래스 변수 vs 인스턴스 변수**
```python
class Character:
    # 클래스 변수 - 모든 인스턴스가 공유
    all_characters = []
    next_id = 1
    
    def __init__(self, name):
        # 인스턴스 변수 - 각 객체마다 고유
        self.name = name
        self.hp = 100
```

**포인트:**
- 클래스 변수: 모든 객체가 공유하는 데이터
- 인스턴스 변수: 각 객체마다 다른 값

### 4. **정적 메서드 (@staticmethod)**
```python
@staticmethod
def create_character(char_type, name):
    # 인스턴스 생성 없이 바로 호출 가능
    # self 매개변수 없음
    return Warrior(name)

# 사용법
CharacterManager.create_character('warrior', '아서')  # 인스턴스 없이 호출
```

**포인트:**
- 클래스와 관련있지만 독립적인 유틸리티 함수
- `self` 매개변수 없음
- 인스턴스 생성 없이 바로 호출

---

## 🛠️ 사용된 중요 메서드들

### **핵심 캐릭터 메서드들**
| 메서드 | 설명 | 실제 사용 예시 |
|--------|------|----------------|
| `attack()` | 각 클래스별 고유 공격 | 전투 시 데미지 계산 |
| `take_damage(damage)` | 데미지 받고 HP 감소 | **전투 시스템에서 핵심!** |
| `heal(amount)` | HP 회복 | 마법사 힐링 스킬 |
| `get_info()` | 캐릭터 정보 딕셔너리 반환 | 상세 정보 출력 |

### **기본 메서드들**
| 메서드 | 설명 | 예시 |
|--------|------|------|
| `__init__()` | 객체 초기화 (생성자) | `Character("아서")` |
| `__str__()` | 문자열 표현 정의 | `print(character)` |
| `super()` | 부모 클래스 메서드 호출 | `super().__init__()` |

### **내장 함수들**
| 함수 | 설명 | 예시 |
|------|------|------|
| `isinstance(obj, class)` | 객체 타입 확인 | `isinstance(warrior, Warrior)` |
| `hasattr(obj, attr)` | 속성 존재 확인 | `hasattr(character, 'strength')` |
| `setattr(obj, attr, value)` | 속성 값 설정 | `setattr(character, 'level', 5)` |
| `getattr(obj, attr)` | 속성 값 가져오기 | `getattr(character, 'name')` |

### **문자열 메서드들**
| 메서드 | 설명 | 예시 |
|--------|------|------|
| `.strip()` | 앞뒤 공백 제거 | `"  hello  ".strip()` → `"hello"` |
| `.lower()` | 소문자 변환 | `"WARRIOR".lower()` → `"warrior"` |
| `.title()` | 첫글자 대문자 | `"warrior".title()` → `"Warrior"` |

---

## ⚔️ 전투 시스템 구현

### **1:1 전투 시스템**
```python
def battle_system(attacker, defender):
    """인터랙티브 전투 - 라운드별로 진행"""
    while attacker.hp > 0 and defender.hp > 0:
        # 1. 공격자가 공격
        damage = calculate_damage(attacker)
        
        # 2. 수비자가 데미지 받음 (take_damage 활용!)
        defender.take_damage(damage)
        
        # 3. 승부 판정
        if defender.hp <= 0:
            print(f"{attacker.name} 승리!")
            break
            
        # 4. 턴 교체
        attacker, defender = defender, attacker
```

### **데미지 계산 시스템**
```python
# 클래스별로 다른 데미지 계산
if isinstance(attacker, Warrior):
    damage = attacker.strength + 10      # 물리 공격
elif isinstance(attacker, Mage):
    if attacker.mp >= 10:
        damage = attacker.intelligence + 15  # 마법 공격 (MP 소모)
        attacker.mp -= 10
    else:
        damage = 5  # MP 부족시 약한 공격
elif isinstance(attacker, Archer):
    damage = attacker.dexterity + 18     # 원거리 공격
```

### **HP 관리 시스템**
```python
def take_damage(self, damage):
    """데미지 받기 - 전투의 핵심!"""
    self.hp -= damage
    if self.hp < 0:
        self.hp = 0  # 음수 방지
    return f"{self.name}이(가) {damage} 데미지를 받았다! (HP: {self.hp}/{self.max_hp})"
```

**포인트:**
- 각 클래스마다 **다른 데미지 계산식**
- **턴제 시스템**으로 공정한 전투
- **실시간 HP 감소** 시각화
- **MP 시스템**으로 마법사의 특별함

---

## 🎯 메뉴 시스템 확장

### **기존 메뉴 (1-7번)**
- 캐릭터 생성/조회/수정/삭제
- 단순 공격/스킬 테스트

### **새로 추가된 메뉴 (8-9번)**
| 메뉴 | 기능 | 특징 |
|------|------|------|
| **8. 1:1 전투** | 인터랙티브 전투 | 라운드별 진행, 사용자가 계속/중단 선택 |
| **9. 자동 전투** | 빠른 결과 확인 | 5라운드 자동 진행, HP/MP 자동 복원 |

### **전투 메뉴 사용법**
```python
# 사용 순서
1. 캐릭터 2명 이상 생성
2. 메뉴 8번 또는 9번 선택  
3. 공격자/수비자 ID 입력
4. 전투 결과 확인
```

---

## 🎯 CRUD 구현

### **Create (생성)**
```python
@staticmethod
def create_character(char_type, name):
    char_types = {
        'warrior': Warrior,
        'mage': Mage,
        'archer': Archer
    }
    character = char_types[char_type.lower()](name)
    return character
```

### **Read (조회)**
```python
@staticmethod
def get_character(char_id):
    for char in Character.all_characters:
        if char.id == char_id:
            return char
    return None
```

### **Update (수정)**
```python
@staticmethod
def update_character(char_id, **kwargs):
    character = CharacterManager.get_character(char_id)
    for key, value in kwargs.items():
        setattr(character, key, value)
```

### **Delete (삭제)**
```python
@staticmethod
def delete_character(char_id):
    character = CharacterManager.get_character(char_id)
    Character.all_characters.remove(character)
```

---

## 🧠 고급 파이썬 기법들

### 1. **딕셔너리 매핑**
```python
char_types = {
    'warrior': Warrior,    # 문자열을 클래스에 매핑
    'mage': Mage,
    'archer': Archer
}
character = char_types['warrior']("아서")  # 동적 클래스 생성
```

### 2. **가변 키워드 인자 (**kwargs)**
```python
def update_character(char_id, **kwargs):
    # **kwargs로 여러 속성을 한번에 받음
    # 사용법: update_character(1, level=5, exp=1000)
    for key, value in kwargs.items():
        setattr(character, key, value)
```

### 3. **튜플 언패킹으로 변수 교체**
```python
# 전투에서 턴 교체할 때 사용!
attacker, defender = defender, attacker  # 한 줄로 변수 교체
```

### 4. **백업과 복원 패턴**
```python
# 자동 전투에서 HP/MP 백업
original_hp = character.hp
original_mp = character.mp

# 전투 진행...

# 원래 상태로 복원
character.hp = original_hp
character.mp = original_mp
```

---

## 🔄 다형성 (Polymorphism) 구현

🎭 다형성 = "같은 명령, 다른 행동"

### **전투에서의 다형성**
```python
def calculate_damage(attacker):
    """공격자 타입에 관계없이 데미지 계산"""
    # isinstance()로 타입 확인 후 각각 다른 계산
    if isinstance(attacker, Warrior):
        return attacker.strength + 10
    elif isinstance(attacker, Mage):
        return attacker.intelligence + 15  
    elif isinstance(attacker, Archer):
        return attacker.dexterity + 18

# 사용할 때 - 어떤 캐릭터든 상관없이!
for character in [warrior, mage, archer]:
    damage = calculate_damage(character)  # 각자 다른 방식으로 계산!
```

### **use_skill 함수에서의 다형성**
```python
def use_skill(character):
    """캐릭터 타입에 따라 다른 스킬 실행"""
    if isinstance(character, Warrior):
        return character.shield_block()
    elif isinstance(character, Mage):
        return character.magic_heal()
    elif isinstance(character, Archer):
        return character.double_shot()
```

**장점:**
- 같은 인터페이스로 다른 동작 수행
- 코드 확장성과 유연성 증대

---

## 💡 실전 팁들

### **1. 입력 검증 패턴**
```python
def get_user_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip()
        if valid_options and user_input.lower() not in valid_options:
            print("❌ 올바른 옵션을 선택해주세요")
            continue
        return user_input
```

### **2. 메뉴 시스템 패턴**
```python
def interactive_menu():
    while True:
        choice = input("선택: ").strip()
        
        if choice == '1':
            # 기능 1
        elif choice == '2':
            # 기능 2
        elif choice == '0':
            break
        else:
            print("잘못된 선택")
```

### **3. 데이터 출력 패턴**
```python
def display_info(character):
    info = character.get_info()
    for key, value in info.items():
        print(f"{key}: {value}")
```

---

## 🎯 연습 과제

### **기본 과제**
1. 새로운 캐릭터 클래스 `Priest` 추가해보기
   - 힐링에 특화된 캐릭터
   - `holy_attack()` 고유 스킬
2. 캐릭터 레벨업 시스템 구현
   - 전투 승리시 경험치 획득
   - 레벨업시 스탯 증가
3. **크리티컬 히트 시스템 추가**
   - 10% 확률로 2배 데미지
   - `random` 모듈 활용

### **심화 과제**
1. **장비 시스템 추가**
   - 무기/방어구 착용
   - 장비에 따른 스탯 변화
2. **팀 전투 시스템**
   - 3:3 팀 배틀
   - 턴 순서 관리
3. **AI 전투 시스템**
   - 컴퓨터가 자동으로 최적 행동 선택
   - 간단한 전략 알고리즘

### **전투 시스템 개선 과제**
1. **스킬 시스템 확장**
   ```python
   # 각 캐릭터마다 여러 스킬
   warrior.skills = ['slash', 'shield_block', 'berserker']
   ```
2. **상태이상 시스템**
   - 독, 화상, 빙결 등
   - 턴마다 지속 효과
3. **전투 로그 저장**
   - 전투 기록을 파일로 저장
   - 전적 통계 시스템

---

## 🚀 다음 단계

이 프로젝트를 완전히 이해했다면:
- **모듈과 패키지** 분리 학습 (클래스별 파일 분리)
- **파일 입출력** 으로 캐릭터 데이터 영구 저장
- **예외 처리** 고도화 (커스텀 예외 클래스)
- **GUI 프로그래밍** (tkinter로 시각적 전투)
- **데이터베이스 연동** (SQLite로 캐릭터 관리)
- **네트워크 프로그래밍** (온라인 PvP 전투)

---

## 📊 학습 진도 체크

### ✅ **완전 이해해야 할 개념들**
- [x] 클래스 상속 (`class Child(Parent)`)
- [x] 메서드 오버라이딩 (부모 메서드 재정의)
- [x] `super()` 사용법
- [x] 클래스 변수 vs 인스턴스 변수
- [x] 정적 메서드 (`@staticmethod`)
- [x] `isinstance()` 활용
- [x] 다형성 개념과 실제 구현
- [x] CRUD 패턴
- [x] **메서드 간 연계 (attack → take_damage)**

### 🔥 **전투 시스템 핵심 포인트**
- [x] 턴제 시스템 구현
- [x] 상태 관리 (HP/MP 실시간 변화)
- [x] 클래스별 차별화된 전투 로직
- [x] 사용자 인터랙션 (계속/중단 선택)
- [x] 데이터 백업/복원 패턴

---

## 📁 파일 구조
```
day6/
├── game_character_system.py  # 메인 코드 (전투 시스템 포함)
└── README.md                 # 이 파일 (업데이트됨)
```

## 🎮 실행 방법
```bash
cd python-study/day6
python game_character_system.py
```

### 🎯 **전투 시스템 테스트 순서**
1. 프로그램 실행 → 모드 선택 (1. 인터랙티브)
2. 메뉴 1번으로 캐릭터 2명 이상 생성
3. 메뉴 8번 (1:1 전투) 또는 9번 (자동 전투) 테스트
4. take_damage() 메서드가 실제로 작동하는 것 확인!

---
*이 프로젝트로 상속, 오버라이딩, CRUD, 정적메서드, 전투시스템까지 모두 마스터해보자! ⚔️🔥*