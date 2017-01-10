def modify_list(l):
	a = len(l)
	b = []
	for i in range(0,a):
		if l[i] % 2 == 0:
			b.append(l[i] // 2)
	l.clear()
	for i in b:
		l.append(i)
