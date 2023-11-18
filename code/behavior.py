class StandardBehavior:
      
    def create_file(self):
        print("created")

    def read_file(self):
        print("Read")

    def execute_file(self):
        print("executed")

    def delete_file(self):
        print("Deleted")
        
    def get_behaviors(self):
        return {
            'create_file': StandardBehavior.create_file,
            'read_file': StandardBehavior.read_file,
            'execute_file': StandardBehavior.execute_file,
            'delete_file': StandardBehavior.delete_file
        }
    # 기타 행동 메소드...

class DepartmentEventBehavior:
    def __init__(self, file=None):
        self.employee = employee
        self.file = file

    def special_event_action(self):
        # 특별 이벤트에 맞는 행동 로직
        pass

    # 기타 특별 이벤트 행동 메소드...


class MaliciousBehavior:
    def __init__(self, file=None):
        self.employee = employee
        self.file = file

    def malicious_action1(self):
        # 악의적인 행동 1 로직
        pass

    def malicious_action2(self):
        # 악의적인 행동 2 로직
        pass

    # 기타 악의적인 행동 메소드...
