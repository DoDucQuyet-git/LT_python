from models.employee import Employee
from services.file_service import load_data, save_data

class HRController:
    def __init__(self):
        self.employees = [Employee(**e) for e in load_data()]

    def add_employee(self, data):
        emp = Employee(**data)
        self.employees.append(emp)
        self._save()

    def delete_employee(self, emp_id):
        self.employees = [e for e in self.employees if e.emp_id != emp_id]
        self._save()

    def update_employee(self, emp_id, data):
        for i, e in enumerate(self.employees):
            if e.emp_id == emp_id:
                self.employees[i] = Employee(**data)
        self._save()

    def search(self, keyword):
        return [e for e in self.employees if keyword.lower() in e.name.lower()]

    def get_all(self):
        return self.employees

    def _save(self):
        save_data([e.to_dict() for e in self.employees])