_tuple = ('a', 'b', 'd', 'e')

# Cắt từ đầu đến vị trí 2 (lấy 'a', 'b') + ('c',) + Cắt từ vị trí 2 đến hết
_new_tuple = _tuple[:2] + ('c',) + _tuple[2:]

print("Tuple mới:", _new_tuple) 
# Kết quả: ('a', 'b', 'c', 'd', 'e')