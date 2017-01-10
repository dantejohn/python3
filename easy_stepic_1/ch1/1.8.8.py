X = int(input())
H = int(input())
M = int(input())

H1 = H + X // 60
M1 = M + (X - 60 * (X // 60))

if M1 >= 60:
	H1 += 1
	M1 -= 60
print(H1)
print(M1)
