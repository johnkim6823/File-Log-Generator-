import os
import shutil

base_path = "employees_folders"
central_server = "central_file_server"

class FolderManager:
    def __init__(self, base_path=base_path, central_path = central_server):
        self.base_path = base_path.replace("/", "\\").replace(":", "_").replace(" ", "_")
        self.central_path = central_path.replace("/", "\\").replace(":", "_").replace(" ", "_")

    def create_employee_folders(self, departments):
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

        for department in departments:
            for employee in department.employees:
                employee_folder_path = os.path.join(self.base_path, employee.name)
                if not os.path.exists(employee_folder_path):
                    os.mkdir(employee_folder_path)
 

    def initialize_folders(self):
        print("==============================")
        print("3.1 Initializing folders for employees")
        if os.path.exists(self.base_path):
            shutil.rmtree(self.base_path)
        os.mkdir(self.base_path)
        print("Done")

        print("==============================")
        print("3.2 Initializing centeral file server")
        if os.path.exists(self.central_path):
            shutil.rmtree(self.central_path)
        os.mkdir(self.central_path)
        print("Done")
        print("==============================")