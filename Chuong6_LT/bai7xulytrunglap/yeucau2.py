_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

# Cách dùng dict để giữ đúng thứ tự ban đầu
_new = list(dict.fromkeys(_list))

print("Kết quả 2:", _new) # Output: ['abc', 'xyz', '12', 'ii', '5a']