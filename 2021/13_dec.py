f = open("13_dec.txt", "r")

dots = []
folds = []
for l in f:
    l = l.strip()
    if l:
        if l.find(',') > -1:
            dots.append(list(map(int, l.split(","))))
        else:
            if l.find("x") > -1:
                folds.append(("x", int(l.split("=")[1])))
            elif l.find("y") > -1:
                folds.append(("y", int(l.split("=")[1])))

def dot_count():
    dot_set = set([(x, y) for x, y in dots])
    print(len(dot_set))

for axis, v in folds:
    if axis == "y":
        for dot in dots:
            if dot[1] > v:
                dot[1] = 2*v-dot[1]
    elif axis == "x":
        for dot in dots:
            if dot[0] > v:
                dot[0] = 2*v-dot[0]
    dot_count()

dot_set = set([(x, y) for x, y in dots])
for j in range(10):
    line = ["."]*50
    for i in range(50):
        if (i, j) in dot_set:
            line[i] = "#"
    print("".join(line))
            
