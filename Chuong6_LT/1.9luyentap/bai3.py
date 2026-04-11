_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chan = []
le = []

for x in _list:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

print("List số chẵn:", chan)
print("List số lẻ:", le)