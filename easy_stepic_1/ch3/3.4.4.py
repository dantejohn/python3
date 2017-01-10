lines = []
with open('input.txt') as inf:
    [lines.append([int(score) for score in line.strip().split(';')[1:]]) for line in inf]

with open('output.txt', 'w') as ouf:
    [ouf.write(str(round(sum(scores) / 3, 9)) + '\n') for scores in lines]
    for c in range(3):
        s = 0
        for r in range(len(lines)):
            s += lines[r][c]
        ouf.write(str(round(s / len(lines), 9)) + ' ')
