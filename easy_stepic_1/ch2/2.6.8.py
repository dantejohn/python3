l = int(input())

list = []

for i in range(1, l + 1):
	for j in range(1, i + 1):
		if len(list) == l:
            break
		list.append(i)
for i in range(len(list)):
	print(list[i], end = ' ')
