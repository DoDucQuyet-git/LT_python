# Danh sách cho trước
_list = ['Python', 'AI', 'Code', 'Gemini', 'Data', 'Pro']

# Nhập số n từ bàn phím
n = int(input("Nhập độ dài n: "))

# Tìm các từ có độ dài > n
_new = []
for word in _list:
    if len(word) > n:
        _new.append(word)

print(f"Các từ có độ dài lớn hơn {n} là:", _new)