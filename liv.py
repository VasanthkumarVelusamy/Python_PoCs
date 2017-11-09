import numpy as np
def is_prime(num):
    is_prime = False
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        else:
            is_prime = True
    return is_prime

def queue_and_stack (A):
    s=np.array([])
    q=np.array([])
    for i in A:
        if is_prime(i):
            q=np.append(q,[i])
        else:
            s=np.append(s,[i])

    for i in q:
        print(''.join(str(int(i))),end=' ')

    print('')
    for i in reversed(s):
        print(''.join(str(int(i))),end=' ')

n = int(input())
A = map(int, input().split())

queue_and_stack(A)


