f = open("16_dec.txt", "r")

def h_to_b(s):
    return bin(int(s, 16))[2:].zfill(len(s)*4)

def b_to_i(s):
    r = 0
    for c in s:
        r = r*2 + int(c)
    return r

def parse_literal(s):
    r = 0
    i = 6
    val = ""
    while i < len(s):
        val += s[i+1:i+5]
        if s[i] == "0":
            break
        i += 5
    return i+5, b_to_i(val)

def calc(op, vals):
    if op == 0:
        return sum(vals)
    if op == 1:
        r = 1
        for v in vals:
            r *= v
        return r
    if op == 2:
        return min(vals)
    if op == 3:
        return max(vals)
    if op == 5:
        return 1 if vals[0] > vals[1] else 0
    if op == 6:
        return 1 if vals[0] < vals[1] else 0
    if op == 7:
        return 1 if vals[0] == vals[1] else 0
    return 0

def parse_packet(s):
    i = 0
    ver = s[i:i+3]
    all_ver.append(ver)
    t = s[i+3:i+6]
    op = b_to_i(t)
    if op == 4:
        j, val = parse_literal(s[i:])
        return i+j, val
    else:
        vals = []
        it = s[i+6]
        if it == "0":
            l = b_to_i(s[i+7:i+22])
            start = i+22
            end = i+22+l
            while i < end:
                step, val = parse_packet(s[start:end])
                i = start + step
                vals.append(val)
                start = i
            return i, calc(op, vals)
        else:
            l = b_to_i(s[i+7:i+18])
            if l > 10:
                return
            start = i+18
            for _ in range(l):
                step, val = parse_packet(s[start:])
                i = start + step
                vals.append(val)
                start = i
            return i, calc(op, vals)

for l in f:
    if not l.strip():
        break
    all_ver = []
    packet = l.strip()
    print(packet)
    b = h_to_b(packet)
    _, r = parse_packet(b)
    print(sum([b_to_i(v) for v in all_ver]))
    print(r)

