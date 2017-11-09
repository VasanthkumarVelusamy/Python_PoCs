
x = int(input())
y = int(input())
z = int(input())

N = int(input())

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != N:
                ar.append([])
                ar[p]=[i,j,k]
                p += 1
