class Node:
    def __init__(self):
        self.lval = None
        self.rval = None
        self.left = None
        self.right = None

def snail_to_tree(a):
    node = Node()
    if type(a[0]) == int:
        node.lval = a[0]
    else:
        node.left = snail_to_tree(a[0])
    if type(a[1]) == int:
        node.rval = a[1]
    else:
        node.right = snail_to_tree(a[1])
    return node

def snail_sum(a, b):
    node = Node()
    node.left = a
    node.right = b
    return node

def explode(a):
    prev = None
    exploded = 0
    done = 0
    rexp_val = 0
    def dfs(node, l):
        nonlocal prev, exploded, done, rexp_val
        if l > 4 and not exploded and node.lval is not None and node.rval is not None:
            if prev:
                if prev.rval is not None:
                    prev.rval += node.lval
                elif prev.lval is not None:
                    prev.lval += node.lval
            exploded = 1
            rexp_val = node.rval
            return -1
        if node.left:
            if dfs(node.left, l+1) == -1:
                node.left = None
                node.lval = 0
        else:
            prev = node
            if exploded and not done:
                node.lval += rexp_val
                done = 1
        if node.right:
            if dfs(node.right, l+1) == -1:
                node.right = None
                node.rval = 0
        else:
            prev = node
            if exploded and not done:
                node.rval += rexp_val
                done = 1
    dfs(a, 1)
    return exploded

def split(a):
    splitted = 0
    def dfs(node):
        nonlocal splitted
        if node.left:
            dfs(node.left)
        if not splitted and node.lval and node.lval > 9:
            splitted = 1
            node.left = Node()
            node.left.lval = node.lval//2
            node.left.rval = node.lval-node.left.lval
            node.lval = None
        if node.right:
            dfs(node.right)
        if not splitted and node.rval and node.rval > 9:
            splitted = 1
            node.right = Node()
            node.right.lval = node.rval//2
            node.right.rval = node.rval-node.right.lval
            node.rval = None
    dfs(a)
    return splitted

def mag(node):
    lmag = mag(node.left) if node.left else node.lval
    rmag = mag(node.right) if node.right else node.rval
    return 3*lmag+ 2*rmag

def snail_print(node, l=1):
    if node.lval is not None and node.rval is not None:
        if l > 4:
            return [node.lval, "{}".format(l), node.rval]
        return [node.lval, node.rval]
    if node.lval is not None:
        return [node.lval, snail_print(node.right, l+1)]
    if node.rval is not None:
        return [snail_print(node.left, l+1), node.rval]
    return [snail_print(node.left, l+1), snail_print(node.right, l+1)]
        
def stabilize(node):
    more = 1
    while more:
        more = 0
        if explode(node):
            more = 1
        if not more and split(node):
            more = 1

f = open("18_dec.txt", "r")

node = None
snail_list = []
for l in f:
    a = eval(l)
    snail_list.append(a)
    if not node:
        node = snail_to_tree(a)
    else:
        node = snail_sum(node, snail_to_tree(a))

    stabilize(node)

ans = mag(node)
print(ans)

ans2 = 0
ln = len(snail_list)
for i in range(ln):
    for j in range(ln):
        if i != j:
            snail_add = snail_sum(snail_to_tree(snail_list[i]), snail_to_tree(snail_list[j]))
            stabilize(snail_add)
            mag_sum = mag(snail_add)
            ans2 = max(ans2, mag_sum)

print(ans2)
