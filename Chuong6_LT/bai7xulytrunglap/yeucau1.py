_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
_new = []

for item in _list:
    # Nếu phần tử đó chỉ xuất hiện đúng 1 lần trong list gốc
    if _list.count(item) == 1:
        _new.append(item)

print("Kết quả 1:", _new) # Output: ['xyz', 'ii', '5a']