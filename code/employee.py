from behavior import StandardBehavior

import random

class Employee:
    def __init__(self, name, rank, department):
        self.name = name
        self.rank = rank
        self.department = department.name
        self.is_malicious = False        
        self.event_flags = []       # 부서 이벤트 관련 플래그 및 제어 값 
        self.local_files = []       # 로컬 파일 리스트
        self.behavior_pattern = department.regular_behavior_patterns  # 현재 행동 패턴

    def set_malicious_behavior(self):
        self.is_malicious = True


    def update_behavior_pattern(self, new_pattern):
        pass
        # 행동 패턴 갱신

    def decide_participation(self):
        # 사이클 참여 여부를 무작위로 결정
        return random.choice([True, False])

    def perform_behavior(self):
        if self.behavior_pattern and self.decide_participation(): 
        #     behavior_name = random.choice(list(self.behavior_pattern.behaviors.keys()))
        #     result = self.behavior_pattern.behaviors[behavior_name]()
        #     result
            pass

        else:
            print(f'{self.name} is Not a participant.')

    def target_file():
        pass

    def manage_local_files(self, file_action, file=None):
        # 로컬 파일 관리 (추가, 삭제, 수정 등)
        pass

    # 부가적인 함수

    def print_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Department: {self.department.name}")

    def display_behaviors(self):
        print(f"Behaviors for {self.name} :")
        for behavior_name, behavior_func in self.behavior_pattern.items():
            print(f'{behavior_name}')
        print("--------------------------------------")