# 게임 캐릭터 상속과 오버라이딩 학습

class Character:
    """게임 캐릭터 부모 클래스"""
    
    def __init__(self, name, hp=100, mp=50):
        """캐릭터 초기화"""
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.level = 1
    
    def attack(self):
        """기본 공격 - 자식 클래스에서 오버라이딩할 메서드"""
        damage = 10
        return f"{self.name}이(가) 기본 공격! (데미지: {damage})"
    
    def take_damage(self, damage):
        """데미지 받기"""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return f"{self.name}이(가) {damage} 데미지를 받았다! (현재 HP: {self.hp})"
    
    def get_status(self):
        """캐릭터 상태 조회"""
        return f"{self.name} - HP: {self.hp}/{self.max_hp}, MP: {self.mp}/{self.max_mp}, Lv.{self.level}"
    
    def introduce(self):
        """자기소개 - 자식 클래스에서 오버라이딩"""
        return f"안녕, 나는 {self.name}이야!"


class Warrior(Character):
    """전사 클래스 - Character 상속"""
    
    def __init__(self, name):
        # super()로 부모 클래스의 __init__ 호출
        super().__init__(name, hp=150, mp=30)  # 전사는 HP 높고 MP 낮음
        self.strength = 20  # 전사만의 고유 속성
        self.armor = 10
    
    def attack(self):
        """전사의 공격 - 부모 메서드 오버라이딩"""
        damage = self.strength + 15
        return f"{self.name}이(가) 검으로 강력한 공격! (데미지: {damage})"
    
    def introduce(self):
        """전사의 자기소개 - 부모 메서드 오버라이딩"""
        return f"나는 강력한 전사 {self.name}이다! 힘: {self.strength}, 방어력: {self.armor}"
    
    def shield_block(self):
        """전사만의 특수 스킬"""
        return f"{self.name}이(가) 방패로 공격을 막았다! (방어력: {self.armor})"


class Mage(Character):
    """마법사 클래스 - Character 상속"""
    
    def __init__(self, name):
        super().__init__(name, hp=80, mp=150)  # 마법사는 HP 낮고 MP 높음
        self.intelligence = 25  # 마법사만의 고유 속성
        self.spell_power = 18
    
    def attack(self):
        """마법사의 공격 - 부모 메서드 오버라이딩"""
        if self.mp >= 15:
            self.mp -= 15
            damage = self.intelligence + self.spell_power
            return f"{self.name}이(가) 파이어볼 마법 시전! (데미지: {damage}, 남은 MP: {self.mp})"
        else:
            # MP가 부족할 때는 기본 공격
            damage = 5
            return f"{self.name}의 MP가 부족해서 지팡이로 때렸다... (데미지: {damage})"
    
    def introduce(self):
        """마법사의 자기소개 - 부모 메서드 오버라이딩"""
        return f"나는 현명한 마법사 {self.name}이다! 지능: {self.intelligence}, 마법력: {self.spell_power}"
    
    def magic_heal(self, target):
        """마법사만의 특수 스킬 - 힐링"""
        if self.mp >= 20:
            self.mp -= 20
            heal_amount = self.intelligence // 2
            target.hp += heal_amount
            if target.hp > target.max_hp:
                target.hp = target.max_hp
            return f"{self.name}이(가) {target.name}을 {heal_amount} 치료했다! ({target.name} HP: {target.hp})"
        else:
            return f"{self.name}의 MP가 부족해서 치료할 수 없다!"


class Archer(Character):
    """궁수 클래스 - Character 상속"""
    
    def __init__(self, name):
        super().__init__(name, hp=120, mp=80)  # 균형잡힌 스탯
        self.dexterity = 22  # 궁수만의 고유 속성
        self.accuracy = 18
    
    def attack(self):
        """궁수의 공격 - 부모 메서드 오버라이딩"""
        damage = self.dexterity + self.accuracy
        return f"{self.name}이(가) 화살로 정확히 조준 사격! (데미지: {damage})"
    
    def introduce(self):
        """궁수의 자기소개 - 부모 메서드 오버라이딩"""
        return f"나는 민첩한 궁수 {self.name}이다! 민첩: {self.dexterity}, 정확도: {self.accuracy}"
    
    def power_shot(self):
        """궁수만의 특수 스킬 - 강력한 화살"""
        damage = (self.dexterity + self.accuracy) * 2
        return f"{self.name}이(가) 집중해서 강력한 화살을 발사! (데미지: {damage})"

class SuperWarrior(Warrior):
    """전사를 상속받은 슈퍼 전사 - super() 학습용"""
    
    def __init__(self, name):
        super().__init__(name)  # 부모(Warrior)의 __init__ 호출
        self.super_strength = 50  # 추가 속성
    
    def attack(self):
        """부모의 attack에 추가 기능"""
        # 부모의 attack() 결과를 받아와서
        parent_attack = super().attack()
        # 추가 데미지 계산
        extra_damage = self.super_strength
        return f"{parent_attack} + 추가 초강력 공격! (추가 데미지: {extra_damage})"


def test_inheritance_and_overriding():
    """상속과 오버라이딩 테스트"""
    print("=== 게임 캐릭터 상속과 오버라이딩 학습 ===\n")
    
    # 1. 객체 생성 (각각 다른 클래스)
    print("1. 캐릭터 생성")
    warrior = Warrior("아서")
    mage = Mage("간달프") 
    archer = Archer("레골라스")
    
    characters = [warrior, mage, archer]
    
    # 2. 상속 확인 - 부모 클래스의 메서드 사용
    print("\n2. 부모 클래스 메서드 상속 확인")
    for char in characters:
        print(char.get_status())  # 부모 클래스 메서드
    
    # 3. 오버라이딩 확인 - 자기소개
    print("\n3. introduce() 메서드 오버라이딩 확인")
    for char in characters:
        print(char.introduce())  # 각 클래스에서 오버라이딩된 메서드
    
    # 4. 오버라이딩 확인 - 공격
    print("\n4. attack() 메서드 오버라이딩 확인")
    for char in characters:
        print(char.attack())  # 각 클래스에서 오버라이딩된 메서드
    
    # 5. 클래스별 고유 메서드 (다형성)
    print("\n5. 각 클래스의 고유 스킬")
    print(warrior.shield_block())  # 전사만의 스킬
    print(mage.magic_heal(warrior))  # 마법사만의 스킬
    print(archer.power_shot())  # 궁수만의 스킬
    
    # 6. isinstance로 타입 확인
    print("\n6. isinstance()로 타입 확인")
    for char in characters:
        print(f"{char.name}:")
        print(f"  Character의 인스턴스? {isinstance(char, Character)}")
        print(f"  Warrior의 인스턴스? {isinstance(char, Warrior)}")
        print(f"  Mage의 인스턴스? {isinstance(char, Mage)}")
        print(f"  Archer의 인스턴스? {isinstance(char, Archer)}")
        print()
    
    # 7. 다형성 테스트 - 같은 메서드명이지만 다른 동작
    print("7. 다형성 테스트 - 리스트에서 공통 메서드 호출")
    print("모든 캐릭터가 공격!")
    for i, char in enumerate(characters, 1):
        print(f"{i}. {char.attack()}")
    
    # 8. 전투 시뮬레이션
    print("\n8. 간단한 전투 시뮬레이션")
    print(f"{warrior.name} VS {mage.name}")
    print(f"전투 전: {warrior.get_status()}")
    print(f"전투 전: {mage.get_status()}")
    
    # 전사가 마법사 공격
    attack_result = warrior.attack()
    print(f"\n{attack_result}")
    damage = warrior.strength + 15
    damage_result = mage.take_damage(damage)
    print(damage_result)
    
    # 마법사가 자신을 치료
    heal_result = mage.magic_heal(mage)
    print(heal_result)
    
    print(f"\n전투 후: {mage.get_status()}")


def demonstrate_super():
    """super() 사용 예시"""
    print("\n=== super() 사용 방법 학습 ===\n")
    
    # 슈퍼 전사 생성
    super_warrior = SuperWarrior("슈퍼맨")
    print("슈퍼 전사의 공격:")
    print(super_warrior.attack())
    print(f"슈퍼 전사 스탯: 힘 {super_warrior.strength}, 초강력 {super_warrior.super_strength}")


if __name__ == "__main__":
    # 메인 테스트 실행
    test_inheritance_and_overriding()
    
    # super() 예시
    demonstrate_super()
    
    # print("\n=== 학습 포인트 ===")
    # print("1. 상속: 자식 클래스가 부모 클래스의 속성과 메서드를 물려받음")
    # print("2. 오버라이딩: 자식 클래스에서 부모의 메서드를 재정의")
    # print("3. super(): 부모 클래스의 메서드나 생성자 호출")
    # print("4. 다형성: 같은 메서드명으로 다른 동작 수행")
    # print("5. isinstance(): 객체의 타입 확인")