'''
import numpy as np
def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
    return is_prime

def queue_and_stack (A):
    result=[]
    s=np.array([])
    q=np.array([])
    for i in A:
        if is_prime(i):
            queue_list.insert(q,i)
        else:
            stack_list.insert(s,i,0)
    result.append(queue_list)
    result.append(reversed(stack_list))
    return result


n = int(input())
A = map(int, input().split())

out_ = queue_and_stack(A)
for i_out_ in out_:
    print (' '.join(map(str, i_out_)))

'''



import math
def is_prime(a):
    return all(a % i for i in range(2, a))
# def is_prime(num):
#     is_prime = False
#     sq = int(math.sqrt(num))
#     if num > 1:
#         for i in range(2,sq+1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         else:
#             is_prime = True
#     return is_prime

def queue_and_stack (A):
    s=[]
    q=[]
    for i in A:
        if is_prime(i):
            q.append(i)
        else:
            s.append(i)

    for i in q:
        print(''.join(str(i)),end = ' ')

    print('')
    for i in reversed(s):
        print(''.join(str(i)),end=' ')


n = int(input())
A = map(int, input().split())

queue_and_stack(A)
