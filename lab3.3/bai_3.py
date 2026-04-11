import time

# Lấy năm hiện tại từ hệ thống
x = time.localtime()
year_now = x[0]

nam_sinh = int(input("Nhập vào năm sinh của bạn: "))
tuoi = year_now - nam_sinh

print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")