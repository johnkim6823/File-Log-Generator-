import random

class Employee:
    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department
        self.is_in_event = False
        self.local_files = []
        self.behavior_patterns = self.department.normal_behavior_patterns.get(grade, [])
    
    def decide_action(self):
        if self.is_in_event and self.department.event_behavior_patterns:
            # 부서 이벤트 관련 행동 패턴 사용
            return random.choice(self.department.event_behavior_patterns)
        elif self.behavior_patterns:
            # 개인 행동 패턴 사용
            return random.choice(self.behavior_patterns)
        else:
            # 기본 행동
            return "일반 작업"

    def update_behavior_pattern(self, new_pattern):
        self.behavior_patterns = new_pattern

    def perform_action(self):
        action = self.decide_action()
        print(f"{self.name} (Grade: {self.grade}) is performing: {action}")

    def manage_local_files(self, file_action, file_name=None):
        # 로컬 파일 관리 로직 구현 필요
        pass

    # 추가적인 메서드들(예: 협업 이벤트 플래그 관리, 타겟 랜덤 지정 등) 구현 필요
