a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d + 1):
	print(i, end = '\t')
print()
for j in range(a, b + 1):
	print(j, end = '\t')
	for i in range(c, d + 1):
		print(i * j, end = '\t')
	print(end = '\n')
