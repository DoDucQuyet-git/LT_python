def giai_thua(n):
    if n == 0:
        return 1
    return n * giai_thua(n - 1)

number = 5
print(f"Giai thừa của {number} là: {giai_thua(number)}")