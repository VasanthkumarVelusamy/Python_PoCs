import cProfile

n, q = input().split()
N=int(n)
Q=int(q)
A = list(map(int, input().split()))
listx = []
listy = []
result = []

@profile
def min_dis():
    res = []
    for x in listx:
        for y in listy:

            dir_mean = y - x
            if dir_mean > 0:
                cir_mean = x + (N - y)
            if dir_mean < 0:
                cir_mean = y + (N - x)
            if abs(dir_mean) < cir_mean:
                res.append(abs(dir_mean)//2)
            else:
                res.append(abs(cir_mean)//2)
    result.append(min(res))

while Q > 0:
    i, j = -1,-1
    Q -= 1
    x,y = list(map(int, input().split()))
    while True:
        try:
            i = A[i+1:].index(x) + i + 1
            listx.append(i)
        except ValueError:
            break
    while True:
        try:
            j = A[j+1:].index(y) + j + 1
            listy.append(j)
        except ValueError:
            break
    #cProfile.run('min_dis()')
    min_dis()
    listx.clear()
    listy.clear()

for k in result:
    print(k)
