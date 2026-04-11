import tkinter as tk
from tkinter import ttk, messagebox


class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("HR Management System")
        self.root.geometry("1100x600")
        self.root.configure(bg="#f4f6f9")

        self._setup_style()
        self._build_ui()
        self.refresh()

    # ================= STYLE =================
    def _setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white")

        style.configure("Treeview.Heading",
                        font=("Arial", 10, "bold"),
                        background="#2c3e50",
                        foreground="white")

    # ================= UI =================
    def _build_ui(self):
        # TITLE
        title = tk.Label(self.root,
                         text="HỆ THỐNG QUẢN LÝ NHÂN SỰ",
                         font=("Arial", 18, "bold"),
                         bg="#f4f6f9",
                         fg="#2c3e50")
        title.pack(pady=10)

        # FORM
        form_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.GROOVE)
        form_frame.pack(padx=20, pady=10, fill="x")

        labels = ["ID", "Tên", "Tuổi", "Phòng ban", "Lương"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(form_frame,
                     text=text,
                     bg="white",
                     font=("Arial", 10, "bold")
                     ).grid(row=0, column=i, padx=10, pady=5)

            entry = tk.Entry(form_frame,
                             font=("Arial", 10),
                             bd=2,
                             relief=tk.GROOVE)

            entry.grid(row=1, column=i, padx=10, pady=5)
            self.entries[text] = entry

        # BUTTONS
        btn_frame = tk.Frame(self.root, bg="#f4f6f9")
        btn_frame.pack(pady=10)

        self._create_button(btn_frame, "Thêm", self.add, "#27ae60", 0)
        self._create_button(btn_frame, "Xóa", self.delete, "#e74c3c", 1)
        self._create_button(btn_frame, "Cập nhật", self.update, "#f39c12", 2)
        self._create_button(btn_frame, "Tìm kiếm", self.search, "#2980b9", 3)
        self._create_button(btn_frame, "Reload", self.refresh, "#7f8c8d", 4)

        # TABLE
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        columns = ["ID", "Tên", "Tuổi", "Phòng ban", "Lương"]

        self.tree = ttk.Treeview(table_frame,
                                 columns=columns,
                                 show='headings')

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)

        scrollbar = ttk.Scrollbar(table_frame,
                                  orient="vertical",
                                  command=self.tree.yview)

        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<ButtonRelease-1>", self.select)

    def _create_button(self, frame, text, cmd, color, col):
        btn = tk.Button(frame,
                        text=text,
                        command=cmd,
                        bg=color,
                        fg="white",
                        font=("Arial", 10, "bold"),
                        width=12,
                        bd=0)
        btn.grid(row=0, column=col, padx=5)

    # ================= DATA =================
    def _get_data(self):
        return {
            "emp_id": self.entries["ID"].get(),
            "name": self.entries["Tên"].get(),
            "age": self.entries["Tuổi"].get(),
            "department": self.entries["Phòng ban"].get(),
            "salary": self.entries["Lương"].get()
        }

    # ================= FUNCTIONS =================
    def refresh(self, data=None):
        for row in self.tree.get_children():
            self.tree.delete(row)

        data = data if data else self.controller.get_all()

        for e in data:
            self.tree.insert("",
                             tk.END,
                             values=(e.emp_id,
                                     e.name,
                                     e.age,
                                     e.department,
                                     e.salary))

    def add(self):
        try:
            data = self._get_data()

            if not data["emp_id"] or not data["name"]:
                raise ValueError("Không được để trống ID hoặc Tên")

            self.controller.add_employee(data)
            self.refresh()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def delete(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("Thông báo", "Chọn nhân viên cần xóa")
            return

        emp_id = self.tree.item(selected[0])['values'][0]
        self.controller.delete_employee(emp_id)
        self.refresh()

    def update(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("Thông báo", "Chọn nhân viên cần sửa")
            return

        emp_id = self.tree.item(selected[0])['values'][0]
        self.controller.update_employee(emp_id, self._get_data())
        self.refresh()

    def search(self):
        keyword = self.entries["Tên"].get()

        if not keyword:
            self.refresh()
            return

        result = self.controller.search(keyword)
        self.refresh(result)

    def select(self, event):
        selected = self.tree.selection()

        if selected:
            values = self.tree.item(selected[0])['values']
            keys = ["ID", "Tên", "Tuổi", "Phòng ban", "Lương"]

            for i, key in enumerate(keys):
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, values[i])