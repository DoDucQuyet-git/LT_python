_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

# Nhập giá trị độ dài tối thiểu
n = int(input("Nhập độ dài tối thiểu (ví dụ 4): "))

count = 0
for s in _list:
    # Kiểm tra đồng thời 2 điều kiện
    if len(s) >= n and s[0] == s[-1]:
        count += 1

print("Số lượng chuỗi thỏa mãn là:", count)