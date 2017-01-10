list = [int(i) for i in input().split()]
l = int(input())

c = 0

for i in range(len(list)):
	if l == list[i]:
		c += 1
		print(i, end = ' ')
if c == 0:
    print('Отсутствует')
