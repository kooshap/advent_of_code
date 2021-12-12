f = open("12_dec.txt", "r")

from collections import defaultdict

graph = defaultdict(list)
for l in f:
    nodes = l.strip().split("-")
    a, b = nodes
    graph[a].append(b)
    graph[b].append(a)

visited = defaultdict(int)
exc = set()

print(graph)
def dfs(node):
    if node == "end":
        return 1
    ans = 0
    for nei in graph[node]:
        if nei != "start" and (not nei.islower() or not visited[nei] or not exc):
            if nei.islower() and visited[nei]:
                exc.add(nei)
            visited[nei] += 1
            ans += dfs(nei)
            visited[nei] -= 1
            if nei.islower() and visited[nei]:
                exc.remove(nei)

    return ans

print(dfs("start"))
