#complete this function to return a list that contains answer for all the queries of nodes
def solve(n , u , v , q , nodes):


n = eval(input())
u = list(range(n))
v = list(range(n))
for i in range(0,n-1):
    u[i],v[i] = list(map(int, input().split()))

q = eval(input())
nodes = list(range(q))
for i in range(0,q):
    nodes[i] = eval(input())

ans = solve(n , u , v , q, nodes)
for x in ans:
    print(x)
