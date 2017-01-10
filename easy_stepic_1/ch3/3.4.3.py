with open('input.txt') as inf:
    textfile, matrix, i, d = [], [], 0, {}
    for line in inf:
        textfile.append(line.strip().split())
    for a in range(len(textfile)):
        for b in range(len(textfile[a])):
            if textfile[a][b] in d:
                d[textfile[a][b]]  += 1
            else:
                d[textfile[a][b]] = 1
    max = 0
    name = str("")
    for key,value in d.items():
        if max < value:
            max = value
            name = key
    print(name, max)
