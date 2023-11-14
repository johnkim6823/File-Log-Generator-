import time

class File:
    def __init__(self, name, grade, department, owner):
        self.name = name
        self.grade = grade
        self.department = department
        self.owner = owner
        self.read_permissions = []
        self.write_permissions = []
        self.execute_permissions = []
        self.creation_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.last_updated_time = self.creation_time

    def update_last_modified(self):
        self.last_updated_time = time.strftime("%Y-%m-%d %H:%M:%S")

    def add_read_permission(self, employee):
        if employee not in self.read_permissions:
            self.read_permissions.append(employee)

    def add_write_permission(self, employee):
        if employee not in self.write_permissions:
            self.write_permissions.append(employee)

    def add_execute_permission(self, employee):
        if employee not in self.execute_permissions:
            self.execute_permissions.append(employee)

    # 추가적인 메서드들(예: 파일 내용 변경, 권한 변경 등) 구현 필요
