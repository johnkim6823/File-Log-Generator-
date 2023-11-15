import time

class File:
    def __init__(self, name, grade, department, owner):
        self.name = name                                            # 파일 이름
        self.grade = grade                                          # 파일 등급
        self.department = department                                # 파일이 속한 부서
        self.owner = owner                                          # 파일 만든 사람
        self.read_permissions = []                                  # 읽기 권한 있는 직원
        self.write_permissions = []                                 # 쓰기 권한 있는 직원
        self.execute_permissions = []                               # 실행 권한 있는 직원
        self.creation_time = time.strftime("%Y-%m-%d %H:%M:%S")     # 파일 생성 시간
        self.last_updated_time = self.creation_time                 # 파일 갱신 시간 

    # 파일 갱신 시간 modify 함수
    def update_last_modified(self):                   
        self.last_updated_time = time.strftime("%Y-%m-%d %H:%M:%S")
    


    # 추가적인 메서드들(예: 파일 내용 변경, 권한 변경 등) 구현 필요
