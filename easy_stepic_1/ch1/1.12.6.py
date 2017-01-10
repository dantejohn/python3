a = int(input())

if (a % 10 >= 5 or 10 <= a % 100 <= 20 or a % 10 == 0):
    print(a, 'программистов')
elif (a % 10 == 1 and not 10 <= a % 100 <= 20):
    print(a, 'программист')
else:
    print (a, 'программиста')
