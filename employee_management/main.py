# ======================================
# EMS CLI VERSION (NO GUI)
# ======================================

employees = {}
roles = ["Manager", "Developer", "Intern"]

# Seed data
for i in range(1, 11):
    employees[f"E{i:02}"] = {
        "name": f"NV{i}",
        "age": 20 + i,
        "email": f"nv{i}@gmail.com",
        "salary": 800 + i * 50,
        "projects": [f"P{i}"] if i % 2 == 0 else [],
        "score": i % 10,
        "role": roles[i % 3]
    }

# ================= BUSINESS =================
def calc_salary(emp):
    base = emp["salary"]
    role = emp.get("role", "Intern")

    if role == "Manager":
        return base * 2 + emp["score"] * 100
    elif role == "Developer":
        return base * 1.5 + len(emp["projects"]) * 200
    else:
        return base + emp["score"] * 50


def classify(score):
    if score >= 9:
        return "Xuất sắc"
    elif score >= 7:
        return "Khá"
    elif score >= 5:
        return "TB"
    return "Yếu"


# ================= FUNCTIONS =================
def show_all(data=None):
    data = data if data else employees
    if not data:
        print("❌ Không có dữ liệu")
        return

    print("\n===== DANH SÁCH NHÂN VIÊN =====")
    for emp_id, emp in data.items():
        print(f"{emp_id} | {emp['name']} | {emp['age']} | {emp['role']} | "
              f"Projects: {len(emp['projects'])} | Score: {emp['score']} | "
              f"{classify(emp['score'])} | Salary: {int(calc_salary(emp))}")


def add_employee():
    try:
        emp_id = input("ID: ")
        if emp_id in employees:
            print("❌ Trùng ID")
            return

        name = input("Tên: ")
        age = int(input("Tuổi: "))
        email = input("Email: ")
        salary = float(input("Lương: "))
        role = input("Role (Manager/Developer/Intern): ") or "Intern"

        employees[emp_id] = {
            "name": name,
            "age": age,
            "email": email,
            "salary": salary,
            "projects": [],
            "score": 0,
            "role": role
        }

        print("✔ Đã thêm")
    except:
        print("❌ Lỗi nhập dữ liệu")


def delete_employee():
    emp_id = input("ID cần xóa: ")
    if emp_id in employees:
        del employees[emp_id]
        print("✔ Đã xóa")
    else:
        print("❌ Không tồn tại")


def assign_project():
    try:
        emp_id = input("ID: ")
        project = input("Tên project: ")

        emp = employees[emp_id]
        if len(emp["projects"]) >= 5:
            print("❌ Max 5 project")
            return

        emp["projects"].append(project)
        print("✔ Đã giao project")
    except:
        print("❌ Không tìm thấy nhân viên")


def evaluate():
    try:
        emp_id = input("ID: ")
        score = float(input("Score (0-10): "))

        if not 0 <= score <= 10:
            print("❌ Score phải 0-10")
            return

        employees[emp_id]["score"] = score
        print("✔ Đã đánh giá")
    except:
        print("❌ Lỗi")


def search():
    key = input("Nhập tên cần tìm: ").lower()
    result = {k: v for k, v in employees.items() if key in v["name"].lower()}
    show_all(result)


def top10():
    data = dict(sorted(employees.items(), key=lambda x: len(x[1]["projects"]), reverse=True)[:10])
    show_all(data)


def stats():
    total = len(employees)
    avg = sum(e["score"] for e in employees.values()) / total if total else 0
    total_projects = sum(len(e["projects"]) for e in employees.values())

    print("\n===== THỐNG KÊ =====")
    print(f"Tổng nhân sự: {total}")
    print(f"Score trung bình: {avg:.2f}")
    print(f"Tổng dự án: {total_projects}")


# ================= MENU =================
def menu():
    while True:
        print("\n========= MENU =========")
        print("1. Hiển thị danh sách")
        print("2. Thêm nhân viên")
        print("3. Xóa nhân viên")
        print("4. Giao dự án")
        print("5. Đánh giá")
        print("6. Tìm kiếm")
        print("7. Top 10 project")
        print("8. Thống kê")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            assign_project()
        elif choice == "5":
            evaluate()
        elif choice == "6":
            search()
        elif choice == "7":
            top10()
        elif choice == "8":
            stats()
        elif choice == "0":
            break
        else:
            print("❌ Sai lựa chọn")


# RUN
menu()