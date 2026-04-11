_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
temp_list = []

for item in _tuple:
    # Chỉ lấy những phần tử xuất hiện duy nhất 1 lần
    if _tuple.count(item) == 1:
        temp_list.append(item)

_new_tuple = tuple(temp_list)
print("Kết quả loại bỏ phần tử trùng:", _new_tuple)
# Kết quả: ('b', 'c', 'd')