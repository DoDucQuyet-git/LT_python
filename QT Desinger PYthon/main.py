import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import sqlite3

# ====== DATABASE ======
conn = sqlite3.connect("nhansu.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nhansu (
    cccd TEXT PRIMARY KEY,
    hoten TEXT,
    ngaysinh TEXT,
    gioitinh TEXT,
    diachi TEXT
)
""")
conn.commit()

# ====== HÀM ======
def them():
    try:
        cursor.execute("INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)",
                       (cccd.get(), hoten.get(), ngaysinh.get(), gioitinh.get(), diachi.get()))
        conn.commit()
        messagebox.showinfo("OK", "Thêm thành công")
        hien_thi()
    except:
        messagebox.showerror("Lỗi", "CCCD đã tồn tại!")

def hien_thi():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM nhansu")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def xoa():
    selected = tree.selection()
    if not selected:
        return
    cccd_val = tree.item(selected[0])['values'][0]
    cursor.execute("DELETE FROM nhansu WHERE cccd=?", (cccd_val,))
    conn.commit()
    hien_thi()

def sua():
    cursor.execute("""
    UPDATE nhansu SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
    WHERE cccd=?
    """, (hoten.get(), ngaysinh.get(), gioitinh.get(), diachi.get(), cccd.get()))
    conn.commit()
    hien_thi()

def tim():
    for row in tree.get_children():
        tree.delete(row)
    keyword = timkiem.get()
    cursor.execute("""
    SELECT * FROM nhansu
    WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def chon(event):
    selected = tree.selection()
    if selected:
        values = tree.item(selected[0])['values']
        cccd.set(values[0])
        hoten.set(values[1])
        ngaysinh.set(values[2])
        gioitinh.set(values[3])
        diachi.set(values[4])

# ====== UI ======
root = tk.Tk()
root.title("Quản lý nhân sự")
root.geometry("900x550")
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("Treeview", rowheight=25)

cccd = tk.StringVar()
hoten = tk.StringVar()
ngaysinh = tk.StringVar()
gioitinh = tk.StringVar()
diachi = tk.StringVar()
timkiem = tk.StringVar()

# ====== FRAME FORM ======
form = tk.LabelFrame(root, text="Thông tin nhân sự", padx=20, pady=15, bg="#ffffff", font=("Arial", 12, "bold"))
form.pack(padx=20, pady=15, fill="x")

# dòng 1
tk.Label(form, text="CCCD:", bg="#ffffff").grid(row=0, column=0, padx=10, pady=8, sticky="w")
tk.Entry(form, textvariable=cccd, width=25).grid(row=0, column=1, padx=10)

tk.Label(form, text="Giới tính:", bg="#ffffff").grid(row=0, column=2, padx=10)
ttk.Combobox(form, textvariable=gioitinh, values=["Nam", "Nữ"], width=22).grid(row=0, column=3, padx=10)

# dòng 2
tk.Label(form, text="Họ tên:", bg="#ffffff").grid(row=1, column=0, padx=10, pady=8)
tk.Entry(form, textvariable=hoten, width=25).grid(row=1, column=1, padx=10)

tk.Label(form, text="Ngày sinh:", bg="#ffffff").grid(row=1, column=2)
DateEntry(form, textvariable=ngaysinh, date_pattern="dd/mm/yyyy", width=20).grid(row=1, column=3, padx=10)

# dòng 3
tk.Label(form, text="Địa chỉ:", bg="#ffffff").grid(row=2, column=0, padx=10, pady=8)
tk.Entry(form, textvariable=diachi, width=60).grid(row=2, column=1, columnspan=3, padx=10)

# ====== BUTTON ======
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Thêm", width=10, bg="#4CAF50", fg="white", command=them).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Sửa", width=10, bg="#2196F3", fg="white", command=sua).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Xóa", width=10, bg="#f44336", fg="white", command=xoa).grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="Hiển thị", width=10, bg="#9E9E9E", fg="white", command=hien_thi).grid(row=0, column=3, padx=10)

# ====== SEARCH ======
search_frame = tk.Frame(root, bg="#f0f4f7")
search_frame.pack(pady=10)

tk.Entry(search_frame, textvariable=timkiem, width=40).grid(row=0, column=0, padx=10)
tk.Button(search_frame, text="Tìm kiếm", command=tim).grid(row=0, column=1)

# ====== TABLE ======
tree = ttk.Treeview(root, columns=("cccd", "hoten", "ngaysinh", "gioitinh", "diachi"), show="headings")
tree.heading("cccd", text="CCCD")
tree.heading("hoten", text="Họ tên")
tree.heading("ngaysinh", text="Ngày sinh")
tree.heading("gioitinh", text="Giới tính")
tree.heading("diachi", text="Địa chỉ")

tree.pack(padx=20, pady=15, fill="both", expand=True)
tree.bind("<<TreeviewSelect>>", chon)

hien_thi()
root.mainloop()