
print("Wprowadź liczbę krawędzi i wierzchołków w grafie: ")
n = int(input())
m = int(input())

gr = [[]]*(n+5)
print (gr)

was = []
for x in range(0, n+5):
    was.append(False)

print (was)

for x in range(0, m):
    v1 = int (input())
    v2 = int (input ())
    gr[v1].append(v2)
    gr[v2].append(v1)

def dfs(v):
    print("Wierzchołek nr: ", v)
    was[v]=True
    for x in range (0, len(gr[v])):
        u = gr[v][x]
        if was[u] != True:
            dfs(u)
    return 

for x in range (1, n + 1):
    if was[x] != True:
        dfs(x)

