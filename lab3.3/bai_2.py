_a = int(input("Nhập cạnh a: "))
_b = int(input("Nhập cạnh b: "))
_c = int(input("Nhập cạnh c: "))

# Điều kiện: a+b > c và a+c > b và b+c > a
if (_a + _b > _c) and (_a + _c > _b) and (_b + _c > _a):
    print("Độ dài ba cạnh tam giác")
else:
    print("Đây không phải độ dài ba cạnh tam giác")