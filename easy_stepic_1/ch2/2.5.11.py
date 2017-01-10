list = input().split()
list2 = []
for i in list:
	if list.count(i) >= 2 and i not in list2:
		list2.append(i)
for i in list2:
	print(i, end = ' ')
