list = [int(i) for i in input().split()]
if len(list) == 1:
	print(list[0])
else:
	for j in range(0, len(list)):
		if j == 0:
			print(list[1] + list[-1], sep = ' ', end = ' ')
		elif j == len(list) - 1:
			print(list[j - 1] + list[0], sep = ' ', end = ' ')
		else:
			print(list[j - 1] + list[j+1], sep = ' ', end = ' ')
