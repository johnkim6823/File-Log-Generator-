import random

class Employee:
    def __init__(self, name, rank, department):
        self.name = name
        self.rank = rank
        self.department = department
        self.is_malicious = False        
        self.event_flags = []       # 부서 이벤트 관련 플래그 및 제어 값 
        self.local_files = []       # 로컬 파일 리스트
        self.behavior_pattern = {}  # 현재 행동 패턴

    def set_malicious_behavior(self):
        self.is_malicious = True

    def print_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Department: {self.department.name}")

        
    def update_behavior_pattern(self, new_pattern):
        pass
        # 행동 패턴 갱신

    def decide_action(self):
        if random.random() < 0.5:
            # 50% 확률로 작업 수행
            return 1
        else:
            return 0

    def perform_action(self, behavior, file):
        if self.is_malicious:
            # 악성 행동 수행 로직
            pass
        else:
            # 정상 행동 수행 로직
            pass

    def target_file():
        pass

    def manage_local_files(self, file_action, file=None):
        # 로컬 파일 관리 (추가, 삭제, 수정 등)
        pass

    # 추가로 필요한 메소드 구현 (예: 행동 타겟 랜덤 지정 등)
