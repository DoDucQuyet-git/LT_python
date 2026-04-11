from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, age, email, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.projects = []
        self.performance = 0

    def assign_project(self, project):
        if len(self.projects) >= 5:
            raise Exception("Nhân viên đã có tối đa 5 dự án")
        self.projects.append(project)

    def evaluate(self, score):
        if not (0 <= score <= 10):
            raise ValueError("Điểm phải từ 0-10")
        self.performance = score

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"{self.emp_id} | {self.name} | {self.age} | {self.email} | Projects: {len(self.projects)}"
