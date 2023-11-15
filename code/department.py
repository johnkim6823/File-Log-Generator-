from behavior import StandardBehavior

class Department:
    def __init__(self, name, behavior):
        self.name = name
        self.employees = []                                                 # 부서 내 직원 객체 리스트
        self.event_flag = False
        self.regular_behavior_patterns = behavior
        self.event_behavior_patterns = {}                                   # 부서 이벤트 시의 행동 패턴

    def manage_event(self, event_type, is_active):
        pass
    
    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def update_employee_behavior(self, employee, behavior_pattern):
        # 직원의 행동 패턴 업데이트
        # 이 메소드는 일반 상태와 이벤트 상태에 따라 다르게 작동할 수 있습니다.
        pass


    def assign_behavior_patterns(self):
        # 부서 이벤트 중 수행하는 행동 패턴을 랜덤하게 생성하여 직원들에게 부여
        pass

    # 부가적인 함수
    def display_behaviors(self):
        print(f"Behaviors for {self.name} Department:")
        for behavior_name, behavior_func in self.regular_behavior_patterns.get_behaviors().items():
            print(f'{behavior_name}')
        print("--------------------------------------")