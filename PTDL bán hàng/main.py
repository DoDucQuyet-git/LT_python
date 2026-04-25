import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.rcParams["font.family"] = "Arial"

# ==========================
# WINDOW
# ==========================
root = tk.Tk()
root.title("HỆ THỐNG QUẢN LÝ & PHÂN TÍCH BÁN HÀNG")
root.geometry("1550x860")
root.configure(bg="#ecf0f1")

df = None
sales_col = None
date_col = None

# ==========================
# HEADER
# ==========================
header = tk.Frame(root, bg="#1f618d", height=70)
header.pack(fill="x")

tk.Label(
    header,
    text="HỆ THỐNG PHÂN TÍCH DỮ LIỆU BÁN HÀNG DOANH NGHIỆP",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#1f618d"
).pack(pady=15)

# ==========================
# BODY
# ==========================
body = tk.Frame(root, bg="#ecf0f1")
body.pack(fill="both", expand=True)

left = tk.Frame(body, width=280, bg="#d6eaf8")
left.pack(side="left", fill="y")

right = tk.Frame(body, bg="white")
right.pack(side="right", fill="both", expand=True)

top_info = tk.Frame(left, bg="#d6eaf8")
top_info.pack(pady=10)

lb_info = tk.Label(
    top_info,
    text="CHƯA MỞ FILE CSV",
    font=("Arial", 12, "bold"),
    justify="left",
    bg="#d6eaf8"
)
lb_info.pack()

# ==========================
# STYLE BUTTON
# ==========================
def enter(e):
    e.widget["bg"] = "#21618c"

def leave(e):
    e.widget["bg"] = "#3498db"

def make_btn(text, cmd):
    b = tk.Button(
        left,
        text=text,
        command=cmd,
        font=("Arial", 11, "bold"),
        bg="#3498db",
        fg="white",
        bd=0,
        width=25,
        pady=8,
        cursor="hand2"
    )
    b.bind("<Enter>", enter)
    b.bind("<Leave>", leave)
    b.pack(pady=5)
    return b

# ==========================
# CLEAR RIGHT
# ==========================
def clear_right():
    for w in right.winfo_children():
        w.destroy()

# ==========================
# LOAD FILE
# ==========================
def open_file():
    global df, sales_col, date_col

    file = filedialog.askopenfilename(
        title="Chọn file CSV",
        filetypes=[("CSV file", "*.csv")]
    )

    if not file:
        return

    try:
        df = pd.read_csv(file, encoding="latin1")
        df.columns = df.columns.str.strip()

        sales_col = None
        date_col = None

        for c in df.columns:
            if "SALES" in c.upper():
                sales_col = c
            if "DATE" in c.upper():
                date_col = c

        if sales_col is None or date_col is None:
            messagebox.showerror("Lỗi", "Không tìm thấy cột SALES hoặc DATE")
            return

        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df["Month"] = df[date_col].dt.month
        df["Year"] = df[date_col].dt.year
        df["Quarter"] = df[date_col].dt.quarter

        tong = df[sales_col].sum()
        dong = len(df)
        cot = len(df.columns)

        lb_info.config(
            text=f"Tổng doanh thu: {tong:,.0f}\nSố dòng: {dong}\nSố cột: {cot}"
        )

        show_data()

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# ==========================
# TABLE
# ==========================
def show_table(data):
    table_frame = tk.Frame(right, bg="white")
    table_frame.pack(fill="both", expand=True)

    tree = ttk.Treeview(table_frame, show="headings")
    tree.pack(side="left", fill="both", expand=True)

    scroll = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    scroll.pack(side="right", fill="y")

    tree.configure(yscrollcommand=scroll.set)

    tree["columns"] = list(data.columns)

    for c in data.columns:
        tree.heading(c, text=c)
        tree.column(c, width=150, anchor="center")

    for _, row in data.iterrows():
        tree.insert("", "end", values=list(row))

# ==========================
# SHOW DATA
# ==========================
def show_data():
    clear_right()
    show_table(df.head(200))

# ==========================
# CHART + TABLE
# ==========================
def draw_chart(data, title, kind="bar", rotate=0):
    clear_right()

    fig, ax = plt.subplots(figsize=(10,5))

    if kind == "bar":
        ax.bar(data.index.astype(str), data.values)
    elif kind == "line":
        ax.plot(data.index, data.values, marker="o", linewidth=3)
    elif kind == "pie":
        ax.pie(data.values, labels=data.index, autopct="%1.1f%%", startangle=90)

    ax.set_title(title)

    plt.xticks(rotation=rotate)

    canvas = FigureCanvasTkAgg(fig, master=right)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="x")

    table = pd.DataFrame({
        "Tên": data.index,
        "Doanh thu": data.values
    })

    show_table(table)

# ==========================
# FUNCTIONS
# ==========================
def month_chart():
    data = df.groupby("Month")[sales_col].sum()
    draw_chart(data, "Doanh Thu Theo Tháng", "line")

def year_chart():
    data = df.groupby("Year")[sales_col].sum()
    draw_chart(data, "Doanh Thu Theo Năm")

def quarter_chart():
    data = df.groupby("Quarter")[sales_col].sum()
    draw_chart(data, "Doanh Thu Theo Quý")

def country_chart():
    if "COUNTRY" not in df.columns:
        messagebox.showwarning("Thông báo", "Không có cột COUNTRY")
        return
    data = df.groupby("COUNTRY")[sales_col].sum().sort_values(ascending=False).head(10)
    draw_chart(data, "Top Quốc Gia", rotate=45)

def product_chart():
    if "PRODUCTLINE" not in df.columns:
        messagebox.showwarning("Thông báo", "Không có cột PRODUCTLINE")
        return
    data = df.groupby("PRODUCTLINE")[sales_col].sum()
    draw_chart(data, "Doanh Thu Theo Loại Hàng", rotate=45)

def pie_chart():
    if "PRODUCTLINE" not in df.columns:
        return
    data = df.groupby("PRODUCTLINE")[sales_col].sum()
    draw_chart(data, "Tỷ Lệ Doanh Thu", "pie")

def export_excel():
    if df is None:
        return
    file = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel", "*.xlsx")]
    )
    if file:
        df.to_excel(file, index=False)
        messagebox.showinfo("Thành công", "Đã xuất Excel")

# ==========================
# SEARCH
# ==========================
search_var = tk.StringVar()

tk.Label(left, text="Tìm kiếm:", bg="#d6eaf8",
         font=("Arial", 11, "bold")).pack(pady=(10,0))

search_entry = tk.Entry(left, textvariable=search_var, font=("Arial", 11))
search_entry.pack(pady=5)

def search_data():
    if df is None:
        return
    txt = search_var.get().lower()

    result = df[df.astype(str).apply(
        lambda x: x.str.lower().str.contains(txt)
    ).any(axis=1)]

    clear_right()
    show_table(result.head(300))

make_btn("MỞ FILE CSV", open_file)
make_btn("Xem dữ liệu", show_data)
make_btn("Doanh thu tháng", month_chart)
make_btn("Doanh thu năm", year_chart)
make_btn("Doanh thu quý", quarter_chart)
make_btn("Theo quốc gia", country_chart)
make_btn("Theo loại hàng", product_chart)
make_btn("Biểu đồ tròn", pie_chart)
make_btn("Tìm kiếm", search_data)
make_btn("Xuất Excel", export_excel)

# ==========================
# START SCREEN
# ==========================
tk.Label(
    right,
    text="CHỌN 'MỞ FILE CSV' ĐỂ BẮT ĐẦU",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="#7f8c8d"
).pack(expand=True)

root.mainloop()