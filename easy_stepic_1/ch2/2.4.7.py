genom = input()

genom += 'm'
c = 1

for i in range(0, len(genom) - 1):
    if genom[i] == genom [i + 1]:
    	c += 1
    else:
    	print(genom[i], c, sep = '', end = '')
    	c = 1
