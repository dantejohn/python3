sum = 0
sumsqr = 0
while True:
    b = int(input())
    sum += b
    sumsqr += b ** 2
    if sum == 0:
        break
print(sumsqr)
