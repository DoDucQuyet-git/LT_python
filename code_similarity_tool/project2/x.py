def tinhFactorial(num):
    if num == 0:
        return 1
    return num * tinhFactorial(num - 1)

n = 5
print(f"Kết quả giai thừa: {tinhFactorial(n)}")