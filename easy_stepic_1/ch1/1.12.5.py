a = int(input())
b = int(input())
c = int(input())

if (a >= b and a >= c):
	if (b > c): print (a, c, b, sep='\n')
	else: print (a, b, c, sep='\n')
elif (b >= a and b >= c):
	if (a > c): print (b, c, a, sep='\n')
	else: print (b, a, c, sep='\n')
elif (c >= a and c >= b):
	if (a > b): print (c, b, a, sep='\n')
	else: print (c, a, b, sep='\n')
