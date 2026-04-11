def validate_age(age):
    if age < 18 or age > 65:
        raise Exception("Tuổi không hợp lệ")


def validate_salary(salary):
    if salary <= 0:
        raise Exception("Lương không hợp lệ")


def validate_email(email):
    if "@" not in email:
        raise ValueError("Email không hợp lệ")