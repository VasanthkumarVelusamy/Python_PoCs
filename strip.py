# my_string = '1234'
#
# my_string = my_string.lstrip('0')
#
# print(my_string)
# import math
#
# num = '002202200'.lstrip('0')
# a,b = 0,0
#
# count=0
# for i in range(1,len(num)):
#     a,b=num[0:i],num[i:]
#
#     if b[0]=='0':
#         continue
#     a=int(a)
#     b=int(b)
#     while a<b:
#         b=math.floor(b/10)
#         if (a == b):
#             count+=1
#             break
# print(count)

def calculate (num):
    import math
    a,b = 0,0

    count=0
    for i in range(1,len(num)):
        a,b=num[0:i],num[i:]
        print(a,b)
        if b[0]=='0':
            continue
        a=int(a)
        b=int(b)
        while a<b:
            # print(a,b)
            b=math.floor(b/10)
            if (a == b):
                print(a,b)
                count+=1
                break
    return count

N = input()

out_ = calculate(N)
print (out_)
