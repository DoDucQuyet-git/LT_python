from exceptions.employee_exceptions import *

class Company:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp):
        if emp.emp_id in self.employees:
            raise DuplicateEmployeeError()
        self.employees[emp.emp_id] = emp

    def remove_employee(self, emp_id):
        if emp_id not in self.employees:
            raise EmployeeNotFoundError(emp_id)
        del self.employees[emp_id]

    def find_employee(self, emp_id):
        if emp_id not in self.employees:
            raise EmployeeNotFoundError(emp_id)
        return self.employees[emp_id]

    def top_10_most_projects(self):
        return sorted(self.employees.values(), key=lambda x: len(x.projects), reverse=True)[:10]

    def top_10_least_projects(self):
        return sorted(self.employees.values(), key=lambda x: len(x.projects))[:10]

    def list_one_project(self):
        return [e for e in self.employees.values() if len(e.projects) == 1]