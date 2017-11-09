
def is_prime(num):
    is_prime = False
    if num > 1:
        print('2 reaches here')
        for i in range(2,num):
            if (num % i) == 0:
                print('2 reaches here')
                is_prime = False
                break
        else:
            is_prime = True
    return is_prime
print(is_prime(int(input().strip())))
