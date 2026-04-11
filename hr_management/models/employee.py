class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = int(age)
        self.department = department
        self.salary = float(salary)

    def to_dict(self):
        return self.__dict__