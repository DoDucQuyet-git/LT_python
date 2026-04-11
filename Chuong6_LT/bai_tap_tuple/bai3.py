_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
temp_list = []

for item in _tuple:
    # Nếu item chưa có trong temp_list thì mới thêm vào
    if item not in temp_list:
        temp_list.append(item)

_new_tuple = tuple(temp_list)
print("Kết quả giữ lại 1 phần tử duy nhất:", _new_tuple)
# Kết quả: ('ab', 'b', 'e', 'c', 'd')