#py
from department import Department
from employee import Employee
from folder_manager import FolderManager

#LIB
import json

#======= Read Dept and Employees from JSON =======#
def create_departments_from_json(json_file_path):
    print("==============================")    
    print("1. Read DEPT/EMPLOYEE data from JSON")
    print("==============================")   
    # Load JSON data
    with open(json_file_path, 'r') as file:
        departments_config = json.load(file)

    departments = {}
    for dept_name, employees in departments_config.items():
        department = Department(dept_name)
        for emp_data in employees:
            employee = Employee(emp_data['name'], emp_data['grade'], department)
            department.add_employee(employee)
        departments[dept_name] = department
    
    print("Done")   
    return departments


#======= Create Department =======# # Not Using
def create_departments(departments_config):
    print("==============================")    
    print("1. Setting up the Dept and employees")
    departments = {}
    for dept_name, employee_info in departments_config.items():
        department = Department(dept_name)
        for grade, count in employee_info.items():
            for _ in range(count):
                employee = Employee(f"{dept_name}_{_+1}", grade, department)
                department.add_employee(employee)
                department.set_normal_behavior(grade, ["작업 수행", "문서 작성"])
        departments[dept_name] = department
    print("==============================")
    return departments

#======= Print Employees by department =======#
def print_employees_by_department(departments):
    print("==============================")    
    print("2. Print Dept and Employees")
    print("==============================")    
    for dept_name, department in departments.items():
        print(f"=== {dept_name} Dept's Employee List ===")
        for employee in department.employees:
            print(f"- {employee.name} grade: {employee.grade}")
    print("==============================")   

#======= Simulation =======#
def simulate_actions(departments):
    print("==============================")
    print("3. Simulating ")
    for dept_name, department in departments.items():
        print(f"=== {dept_name} 부서 ===")
        for employee in department.employees:
            employee.perform_action()

#======= main =======#
def main():
    #1 prerequisite
    json_file_path = './department_data.json'  # Update this path to the actual file location
    departments = create_departments_from_json(json_file_path)

    
    #2
    print_employees_by_department(departments)

    #3
    folder_manager = FolderManager()
    folder_manager.initialize_folders()
    folder_manager.create_employee_folders(departments.values())



if __name__ == "__main__":

    main()
