import tkinter as tk
from tkinter import ttk, messagebox

class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("HR Management System")
        self.root.geometry("1100x600")
        self.root.configure(bg="#f4f6f9")

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

        self._build_ui()
        self.refresh()

    def _build_ui(self):
        # ===== TITLE =====
        title = tk.Label(self.root, text="HỆ THỐNG QUẢN LÝ NHÂN SỰ",
                         font=("Arial", 18, "bold"),
                         bg="#f4f6f9", fg="#2c3e50")
        title.pack(pady=10)

        # ===== FORM =====
        form_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief=tk.GROOVE)
        form_frame.pack(pady=10, padx=20, fill="x")

        labels = ["ID", "Tên", "Tuổi", "Phòng ban", "Lương"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(form_frame, text=text, bg="#ffffff",
                     font=("Arial", 10, "bold")).grid(row=0, column=i, padx=10, pady=5)

            entry = tk.Entry(form_frame, font=("Arial", 10), bd=2, relief=tk.GROOVE)
            entry.grid(row=1, column=i, padx=10, pady=5)
            self.entries[text] = entry

        # ===== BUTTONS =====
        btn_frame = tk.Frame(self.root, bg="#f4f6f9")
        btn_frame.pack(pady=10)

        def create_btn(text, cmd, color):
            return tk.Button(btn_frame, text=text, command=cmd,
                             bg=color, fg="white",
                             font=("Arial", 10, "bold"),
                             width=12, bd=0)

        create_btn("Thêm", self.add, "#27ae60").grid(row=0, column=0, padx=5)
        create_btn("Xóa", self.delete, "#e74c3c").grid(row=0, column=1, padx=5)
        create_btn("Cập nhật", self.update, "#f39c12").grid(row=0, column=2, padx=5)
        create_btn("Tìm kiếm", self.search, "#2980b9").grid(row=0, column=3, padx=5)
        create_btn("Reload", self.refresh, "#7f8c8d").grid(row=0, column=4, padx=5)

        # ===== TABLE =====
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        columns = ["ID", "Tên", "Tuổi", "Phòng ban", "Lương"]
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)
