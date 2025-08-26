# 게임 캐릭터 시스템 - 상속과 CRUD 구현

class Character:
    """게임 캐릭터 부모 클래스"""
    # 클래스 변수 - 모든 캐릭터가 공유하는 데이터
    all_characters = []  # 생성된 모든 캐릭터 저장
    next_id = 1         # 자동 증가 ID
    
    def __init__(self, name, hp=100, mp=50):
        """캐릭터 초기화"""
        # 인스턴스 변수
        self.id = Character.next_id
        Character.next_id += 1
        
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.level = 1
        self.exp = 0
        
        # 생성된 캐릭터를 전체 리스트에 추가
        Character.all_characters.append(self)
    
    def attack(self):
        """기본 공격 - 자식 클래스에서 오버라이딩할 메서드"""
        return f"{self.name}이(가) 기본 공격!"
    
    def take_damage(self, damage):
        """데미지 받기"""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return f"{self.name}이(가) {damage} 데미지를 받았다! (HP: {self.hp}/{self.max_hp})"
    
    def heal(self, amount):
        """회복"""
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return f"{self.name}이(가) {amount} 회복! (HP: {self.hp}/{self.max_hp})"
    
    def get_info(self):
        """캐릭터 정보 조회"""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.__class__.__name__,
            'hp': f"{self.hp}/{self.max_hp}",
            'mp': f"{self.mp}/{self.max_mp}",
            'level': self.level,
            'exp': self.exp
        }
    
    def __str__(self):
        """문자열 표현"""
        return f"[{self.id}] {self.name} ({self.__class__.__name__}) - Lv.{self.level}"


class Warrior(Character):
    """전사 클래스 - Character 상속"""
    
    def __init__(self, name):
        # super()로 부모 클래스 초기화 호출
        super().__init__(name, hp=150, mp=30)  # 전사는 HP 높고 MP 낮음
        self.strength = 20  # 전사만의 고유 속성
        self.armor = 10
    
    def attack(self):
        """전사의 공격 - 부모 메서드 오버라이딩"""
        damage = self.strength + 10
        return f"{self.name}이(가) 칼로 강력하게 공격! (데미지: {damage})"
    
    def shield_block(self):
        """전사만의 특수 스킬"""
        return f"{self.name}이(가) 방패로 막았다! (방어력: {self.armor})"


class Mage(Character):
    """마법사 클래스 - Character 상속"""
    
    def __init__(self, name):
        super().__init__(name, hp=80, mp=120)  # 마법사는 HP 낮고 MP 높음
        self.intelligence = 25  # 마법사만의 고유 속성
        self.spell_power = 15
    
    def attack(self):
        """마법사의 공격 - 부모 메서드 오버라이딩"""
        if self.mp >= 10:
            self.mp -= 10
            damage = self.intelligence + self.spell_power
            return f"{self.name}이(가) 파이어볼 마법 시전! (데미지: {damage}, MP: {self.mp}/{self.max_mp})"
        else:
            return f"{self.name}의 MP가 부족하다!"
    
    def magic_heal(self, target):
        """마법사만의 특수 스킬 - 힐링"""
        if self.mp >= 15:
            self.mp -= 15
            heal_amount = self.intelligence
            return target.heal(heal_amount) + f" (마법사 {self.name}이 치료)"
        else:
            return f"{self.name}의 MP가 부족해서 치료할 수 없다!"


class Archer(Character):
    """궁수 클래스 - Character 상속"""
    
    def __init__(self, name):
        super().__init__(name, hp=110, mp=70)  # 균형잡힌 스탯
        self.dexterity = 22  # 궁수만의 고유 속성
        self.accuracy = 18
    
    def attack(self):
        """궁수의 공격 - 부모 메서드 오버라이딩"""
        damage = self.dexterity + self.accuracy
        return f"{self.name}이(가) 화살로 정확히 명중! (데미지: {damage})"
    
    def double_shot(self):
        """궁수만의 특수 스킬 - 연속 공격"""
        damage = (self.dexterity + self.accuracy) * 2
        return f"{self.name}이(가) 연속 화살 공격! (데미지: {damage})"


class CharacterManager:
    """캐릭터 CRUD 관리 클래스"""
    
    @staticmethod
    def create_character(char_type, name):
        """캐릭터 생성 (Create)"""
        char_types = {
            'warrior': Warrior,
            'mage': Mage,
            'archer': Archer
        }
        
        if char_type.lower() in char_types:
            character = char_types[char_type.lower()](name)
            print(f"✅ {char_type.title()} '{name}' 생성 완료! (ID: {character.id})")
            return character
        else:
            print("❌ 잘못된 캐릭터 타입입니다. (warrior, mage, archer 중 선택)")
            return None
    
    @staticmethod
    def get_character(char_id):
        """특정 캐릭터 조회 (Read)"""
        for char in Character.all_characters:
            if char.id == char_id:
                return char
        return None
    
    @staticmethod
    def get_all_characters():
        """모든 캐릭터 조회 (Read)"""
        return Character.all_characters
    
    @staticmethod
    def update_character(char_id, **kwargs):
        """캐릭터 정보 수정 (Update)"""
        character = CharacterManager.get_character(char_id)
        if character:
            for key, value in kwargs.items():
                if hasattr(character, key):
                    setattr(character, key, value)
                    print(f"✅ {character.name}의 {key}을(를) {value}로 변경했습니다.")
                else:
                    print(f"❌ {key}는 존재하지 않는 속성입니다.")
            return character
        else:
            print(f"❌ ID {char_id}인 캐릭터를 찾을 수 없습니다.")
            return None
    
    @staticmethod
    def delete_character(char_id):
        """캐릭터 삭제 (Delete)"""
        character = CharacterManager.get_character(char_id)
        if character:
            Character.all_characters.remove(character)
            print(f"✅ {character.name} 캐릭터가 삭제되었습니다.")
            return True
        else:
            print(f"❌ ID {char_id}인 캐릭터를 찾을 수 없습니다.")
            return False
    
    @staticmethod
    def display_all_characters():
        """모든 캐릭터 목록 출력"""
        if not Character.all_characters:
            print("등록된 캐릭터가 없습니다.")
            return
        
        print("\n=== 등록된 캐릭터 목록 ===")
        for char in Character.all_characters:
            info = char.get_info()
            print(f"{char} - HP:{info['hp']}, MP:{info['mp']}")
    
    @staticmethod
    def display_character_detail(char_id):
        """특정 캐릭터 상세 정보 출력"""
        character = CharacterManager.get_character(char_id)
        if character:
            print(f"\n=== {character.name} 상세 정보 ===")
            info = character.get_info()
            for key, value in info.items():
                print(f"{key}: {value}")
            
            # 클래스별 고유 속성도 출력
            if isinstance(character, Warrior):
                print(f"strength: {character.strength}")
                print(f"armor: {character.armor}")
            elif isinstance(character, Mage):
                print(f"intelligence: {character.intelligence}")
                print(f"spell_power: {character.spell_power}")
            elif isinstance(character, Archer):
                print(f"dexterity: {character.dexterity}")
                print(f"accuracy: {character.accuracy}")
        else:
            print(f"❌ ID {char_id}인 캐릭터를 찾을 수 없습니다.")


def get_user_input(prompt, valid_options=None):
    """사용자 입력을 받는 헬퍼 함수"""
    while True:
        user_input = input(prompt).strip()
        if valid_options and user_input.lower() not in valid_options:
            print(f"❌ 올바른 옵션을 선택해주세요: {', '.join(valid_options)}")
            continue
        return user_input


def interactive_create_character():
    """사용자 입력으로 캐릭터 생성"""
    print("\n🆕 새 캐릭터 생성")
    print("캐릭터 타입: warrior(전사), mage(마법사), archer(궁수)")
    
    # 캐릭터 타입 입력
    char_type = get_user_input(
        "캐릭터 타입을 선택하세요: ", 
        ['warrior', 'mage', 'archer']
    )
    
    # 캐릭터 이름 입력
    char_name = input("캐릭터 이름을 입력하세요: ").strip()
    
    if not char_name:
        print("❌ 이름을 입력해주세요.")
        return None
    
    # 캐릭터 생성
    character = CharacterManager.create_character(char_type, char_name)
    return character


def battle_system(attacker, defender):
    """1:1 전투 시스템"""
    print(f"\n⚔️ {attacker.name} VS {defender.name} ⚔️")
    print(f"{attacker.name}: HP {attacker.hp}/{attacker.max_hp} | {defender.name}: HP {defender.hp}/{defender.max_hp}")
    
    round_count = 1
    
    while attacker.hp > 0 and defender.hp > 0:
        print(f"\n=== 라운드 {round_count} ===")
        
        # 공격자의 턴
        print(f"\n🗡️ {attacker.name}의 공격!")
        attack_result = attacker.attack()
        print(attack_result)
        
        # 데미지 계산 (클래스별로 다름)
        if isinstance(attacker, Warrior):
            damage = attacker.strength + 10
        elif isinstance(attacker, Mage):
            if attacker.mp >= 10:
                damage = attacker.intelligence + attacker.spell_power
            else:
                damage = 5  # MP 부족시 기본 공격
                print("MP가 부족해서 약한 공격만 가능!")
        elif isinstance(attacker, Archer):
            damage = attacker.dexterity + attacker.accuracy
        else:
            damage = 15  # 기본 데미지
        
        # 수비자가 데미지 받음
        damage_result = defender.take_damage(damage)
        print(damage_result)
        
        # 수비자가 죽었는지 확인
        if defender.hp <= 0:
            print(f"\n🏆 {attacker.name} 승리! {defender.name}이(가) 쓰러졌습니다!")
            break
        
        # 턴 교체 (공격자 ↔ 수비자)
        attacker, defender = defender, attacker
        round_count += 1
        
        # 무한 전투 방지 (10라운드 제한)
        if round_count > 10:
            print("\n⏰ 무승부! 10라운드가 지나 전투가 종료됩니다.")
            break
        
        # 다음 라운드 진행 확인
        continue_battle = input("\n다음 라운드 진행? (엔터: 계속, q: 중단): ").strip().lower()
        if continue_battle == 'q':
            print("전투를 중단합니다.")
            break
    
    print("\n전투 종료!")


def auto_battle(attacker, defender):
    """자동 전투 (빠르게 결과만 보기)"""
    print(f"\n🤖 자동 전투: {attacker.name} VS {defender.name}")
    
    # HP 백업 (전투 후 복원용)
    attacker_original_hp = attacker.hp
    defender_original_hp = defender.hp
    attacker_original_mp = attacker.mp
    defender_original_mp = defender.mp
    
    round_count = 1
    
    while attacker.hp > 0 and defender.hp > 0 and round_count <= 5:
        # 데미지 계산
        if isinstance(attacker, Warrior):
            damage = attacker.strength + 10
        elif isinstance(attacker, Mage):
            if attacker.mp >= 10:
                damage = attacker.intelligence + attacker.spell_power
                attacker.mp -= 10
            else:
                damage = 10
        elif isinstance(attacker, Archer):
            damage = attacker.dexterity + attacker.accuracy
        else:
            damage = 15
        
        # 공격 실행
        print(f"라운드 {round_count}: {attacker.name}이 {damage} 데미지 공격!")
        defender.take_damage(damage)
        
        if defender.hp <= 0:
            print(f"🏆 {attacker.name} 승리!")
            break
        
        # 턴 교체
        attacker, defender = defender, attacker
        round_count += 1
    
    if round_count > 5:
        print("⏰ 무승부!")
    
    # HP/MP 복원 (다른 기능에 영향 주지 않게)
    attacker.hp = attacker_original_hp
    attacker.mp = attacker_original_mp
    defender.hp = defender_original_hp  
    defender.mp = defender_original_mp
    
    print("\n(캐릭터 HP/MP가 원래대로 복원되었습니다)")


def interactive_menu():
    """인터랙티브 메뉴 시스템"""
    print("\n" + "="*50)
    print("🎮 게임 캐릭터 관리 시스템")
    print("="*50)
    
    while True:
        print("\n📋 메뉴를 선택하세요:")
        print("1. 캐릭터 생성")
        print("2. 모든 캐릭터 조회")
        print("3. 캐릭터 상세 정보")
        print("4. 캐릭터 정보 수정")
        print("5. 캐릭터 삭제")
        print("6. 공격 테스트")
        print("7. 스킬 테스트")
        print("8. 1:1 전투")
        print("9. 자동 전투")
        print("0. 종료")
        
        choice = input("\n선택 (0-9): ").strip()
        
        if choice == '1':
            interactive_create_character()
            
        elif choice == '2':
            CharacterManager.display_all_characters()
            
        elif choice == '3':
            if not Character.all_characters:
                print("❌ 등록된 캐릭터가 없습니다.")
                continue
                
            try:
                char_id = int(input("조회할 캐릭터 ID: "))
                CharacterManager.display_character_detail(char_id)
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
                
        elif choice == '4':
            if not Character.all_characters:
                print("❌ 등록된 캐릭터가 없습니다.")
                continue
                
            try:
                char_id = int(input("수정할 캐릭터 ID: "))
                character = CharacterManager.get_character(char_id)
                
                if character:
                    print(f"\n{character.name}의 정보를 수정합니다:")
                    
                    # 레벨 수정
                    level_input = input(f"새 레벨 (현재: {character.level}, 엔터로 건너뛰기): ").strip()
                    if level_input:
                        try:
                            new_level = int(level_input)
                            CharacterManager.update_character(char_id, level=new_level)
                        except ValueError:
                            print("❌ 올바른 숫자를 입력해주세요.")
                    
                    # 경험치 수정
                    exp_input = input(f"새 경험치 (현재: {character.exp}, 엔터로 건너뛰기): ").strip()
                    if exp_input:
                        try:
                            new_exp = int(exp_input)
                            CharacterManager.update_character(char_id, exp=new_exp)
                        except ValueError:
                            print("❌ 올바른 숫자를 입력해주세요.")
                            
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
                
        elif choice == '5':
            if not Character.all_characters:
                print("❌ 등록된 캐릭터가 없습니다.")
                continue
                
            CharacterManager.display_all_characters()
            try:
                char_id = int(input("삭제할 캐릭터 ID: "))
                confirm = input(f"정말 삭제하시겠습니까? (y/N): ").strip().lower()
                if confirm == 'y':
                    CharacterManager.delete_character(char_id)
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
                
        elif choice == '6':
            # 공격 테스트 (기존 전투 테스트)
            if len(Character.all_characters) < 1:
                print("❌ 공격 테스트를 위해서는 최소 1명의 캐릭터가 필요합니다.")
                continue
                
            print("\n⚔️ 공격 테스트")
            CharacterManager.display_all_characters()
            try:
                char_id = int(input("공격할 캐릭터 ID: "))
                character = CharacterManager.get_character(char_id)
                if character:
                    print(f"\n{character.name}의 공격!")
                    print(character.attack())
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
                
        elif choice == '7':
            # 스킬 테스트
            if not Character.all_characters:
                print("❌ 등록된 캐릭터가 없습니다.")
                continue
                
            print("\n🎯 스킬 테스트")
            CharacterManager.display_all_characters()
            try:
                char_id = int(input("스킬을 사용할 캐릭터 ID: "))
                character = CharacterManager.get_character(char_id)
                
                if character:
                    print(f"\n{character.name}의 특수 스킬!")
                    if isinstance(character, Warrior):
                        print(character.shield_block())
                    elif isinstance(character, Mage):
                        # 힐링 대상 선택
                        if len(Character.all_characters) > 1:
                            print("\n힐링 대상을 선택하세요:")
                            CharacterManager.display_all_characters()
                            target_id = int(input("대상 ID: "))
                            target = CharacterManager.get_character(target_id)
                            if target:
                                print(character.magic_heal(target))
                            else:
                                print("❌ 존재하지 않는 캐릭터입니다.")
                        else:
                            print(character.magic_heal(character))  # 자가 힐링
                    elif isinstance(character, Archer):
                        print(character.double_shot())
                        
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
                
        elif choice == '8':
            # 1:1 전투
            if len(Character.all_characters) < 2:
                print("❌ 1:1 전투를 위해서는 최소 2명의 캐릭터가 필요합니다.")
                continue
                
            print("\n⚔️ 1:1 전투")
            CharacterManager.display_all_characters()
            
            try:
                attacker_id = int(input("공격자 캐릭터 ID: "))
                defender_id = int(input("수비자 캐릭터 ID: "))
                
                if attacker_id == defender_id:
                    print("❌ 같은 캐릭터끼리는 전투할 수 없습니다.")
                    continue
                
                attacker = CharacterManager.get_character(attacker_id)
                defender = CharacterManager.get_character(defender_id)
                
                if attacker and defender:
                    battle_system(attacker, defender)
                else:
                    print("❌ 존재하지 않는 캐릭터입니다.")
                    
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
                
        elif choice == '9':
            # 자동 전투
            if len(Character.all_characters) < 2:
                print("❌ 자동 전투를 위해서는 최소 2명의 캐릭터가 필요합니다.")
                continue
                
            print("\n🤖 자동 전투")
            CharacterManager.display_all_characters()
            
            try:
                attacker_id = int(input("공격자 캐릭터 ID: "))
                defender_id = int(input("수비자 캐릭터 ID: "))
                
                if attacker_id == defender_id:
                    print("❌ 같은 캐릭터끼리는 전투할 수 없습니다.")
                    continue
                
                attacker = CharacterManager.get_character(attacker_id)
                defender = CharacterManager.get_character(defender_id)
                
                if attacker and defender:
                    auto_battle(attacker, defender)
                else:
                    print("❌ 존재하지 않는 캐릭터입니다.")
                    
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
                
        elif choice == '0':
            print("\n👋 게임을 종료합니다. 수고하셨습니다!")
            break
            
        else:
            print("❌ 올바른 메뉴를 선택해주세요.")


def demo_mode():
    """데모용 자동 캐릭터 생성"""
    print("\n🤖 데모 모드: 자동으로 캐릭터 3명을 생성합니다...")
    
    # Create - 캐릭터 생성
    warrior = CharacterManager.create_character('warrior', '아서')
    mage = CharacterManager.create_character('mage', '간달프')
    archer = CharacterManager.create_character('archer', '레골라스')
    
    # Read - 캐릭터 조회
    CharacterManager.display_all_characters()
    
    # 상속과 오버라이딩 테스트
    print("\n=== 상속과 오버라이딩 테스트 ===")
    print(warrior.attack())      # 오버라이딩된 전사 공격
    print(mage.attack())         # 오버라이딩된 마법사 공격
    print(archer.attack())       # 오버라이딩된 궁수 공격
    
    # 각 클래스의 고유 스킬 테스트
    print("\n=== 클래스별 고유 스킬 ===")
    print(warrior.shield_block())
    print(mage.magic_heal(warrior))
    print(archer.double_shot())


def main():
    """메인 함수"""
    print("🎮 게임 캐릭터 시스템에 오신 것을 환영합니다!")
    
    mode = get_user_input(
        "\n모드를 선택하세요:\n1. 인터랙티브 모드 (직접 캐릭터 관리)\n2. 데모 모드 (자동 테스트)\n선택 (1/2): ",
        ['1', '2']
    )
    
    if mode == '1':
        interactive_menu()
    else:
        demo_mode()
        print("\n데모가 끝났습니다. 인터랙티브 메뉴로 이동합니다...")
        input("엔터를 눌러 계속...")
        interactive_menu()


if __name__ == "__main__":
    main()
