from employee import Employee
from department import Department
from file import File
from behavior import StandardBehavior

#LIB
import json

department_class_list = []
employees_class_list = [] 
file_clss_list = []

#======= JSON FILE READ =======#
def read_json_file(file_path):
    print("==============================")    
    print("0. Get data from JSON file.")
    with open(file_path, 'r') as file:
        return json.load(file)

#======= Department 클래스 객체 생성 =======#
def create_departments(data, behavior):
    print("==============================")    
    print("1. Make Department 객체.")
    department_class_list = []
    for dept_name in data.keys():
        department = Department(dept_name,behavior)
        department_class_list.append(department)
    return department_class_list

#======= Employee 클래스 객체 생성 =======#
def create_employees(department_class_list, data):
    print("==============================")    
    print("2. Make Employee 객체.")
    employees = []
    for department in department_class_list:
        if department.name in data:
            for emp_data in data[department.name]:
                employee = Employee(emp_data['name'], emp_data['rank'], department)
                employees_class_list .append(employee)
                department.add_employee(employee)
    return employees_class_list 

#======= 객체들 출력 by department_class_list =======#
def print_departments_and_employees(department_class_list):
    print("==============================")    
    print("3.1 Check data by Department")
    print("==============================") 
    for department in department_class_list:
        print(f"Department: {department.name} (Employees: {len(department.employees)})")
        for employee in department.employees:
            print(f" - {employee.name} - RANK: {employee.rank}")


#======= 객체들 출력 by employees_class_list =======#
def print_employee_details(employees_class_list):
    print("==============================")    
    print("3.2 Check data by Department")
    print("==============================") 
    for employee in employees_class_list:
        print(f"Name: {employee.name}, Department: {employee.department}, Rank: {employee.rank}")

#======= Department별 행동들 =======#
def print_department_behavior(department_class_list):
    print("==============================")    
    print("4.1 Check Departments behavior")
    print("==============================") 
    for department in department_class_list:
        department.display_behaviors()

#======= Employee별 행동들 =======#
def print_employee_behavior(employees_class_list):
    print("==============================")    
    print("4.2 Check Departments behavior")
    print("==============================") 
    for employee in employees_class_list:
        employee.display_behaviors()

#======= Simulating =======#
def simulating(employees_class_list):
    for employee in employees_class_list:
        employee.perform_behavior()

def main():
    # JSON 파일 읽기
    data = read_json_file('department_data.json')

    # 행동 객체 생성
    behavior = StandardBehavior()

    # 부서 객체 생성
    department_class_list = create_departments(data, behavior)

    # 직원 객체 생성
    employee_class_list  = create_employees(department_class_list, data)

    #------------------------------------------------------------------------------------
    # # 데이터 출력
    print_departments_and_employees(department_class_list)  # 각 부서별 직원 수와 이름 출력
    print_employee_details(employees_class_list )           # 직원별 상세 정보 출력
    # # 행동 출력 
    # print_department_behavior(department_class_list)
    # print_employee_behavior(employees_class_list)
    #------------------------------------------------------------------------------------

    employee_class_list[0].perform_behavior()

if __name__ == "__main__":
    main()
