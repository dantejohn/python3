stroka = [i.lower() for i in input().split()]
dic = {}
for i in stroka:
    if i in dic:
        dic[i] += 1
    if i not in dic:
        dic[i] = 1
for key, value in dic.items():
    print(key, value) 
