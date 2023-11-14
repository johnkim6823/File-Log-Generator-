import random

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.normal_behavior_patterns = {}  # 직원 등급별 일반 상태 시의 행동 패턴
        self.event_behavior_patterns = {}  # 부서 이벤트 시 행동 패턴

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def set_normal_behavior(self, grade, behaviors):
        self.normal_behavior_patterns[grade] = behaviors

    def set_event_behavior(self, event_type, behaviors):
        self.event_behavior_patterns[event_type] = behaviors

    def manage_department_event(self, event_type):
        if event_type in self.event_behavior_patterns:
            behaviors = self.event_behavior_patterns[event_type]
            for employee in self.employees:
                action = random.choice(behaviors)
                print(f"{employee.name} is performing {action} during {event_type} event.")

    # 부서 인원 변경 관리 메소드 등 추가적인 메서드 구현 필요
