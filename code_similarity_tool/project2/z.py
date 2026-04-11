import math

def check_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

val = 17
if check_prime(val):
    print(f"{val} là số nguyên tố")