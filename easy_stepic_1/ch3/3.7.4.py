c = int(input())

s = {"север": 0, "юг": 0, "восток": 0, "запад": 0}

for i in range(c):
        stroka = input().split()
        s[stroka[0]] += int(stroka[1])

print(s["восток"] - s["запад"], s["север"] - s["юг"], end = " ")
