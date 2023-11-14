# simulation_manager.py
import random
from department import Department
from employee import Employee
import create_folder

class SimulationManager:
    def __init__(self, departments):
        self.departments = departments

    def run_simulation_cycle(self):
        for department in self.departments:
            if random.random() < 0.5:  # 부서별 이벤트 발생 여부 결정
                self.trigger_event(department)

    def trigger_event(self, department):
        selected_employee = random.choice(department.employees)
        selected_employee.perform_action()
