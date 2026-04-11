from models.employee import Employee

class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary * 1.5 + len(self.projects) * 200