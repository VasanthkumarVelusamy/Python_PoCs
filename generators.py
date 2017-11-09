def gen_func():
    for i in range(10):
        print('*')
        yield i*i

my_gen = gen_func()
print(next(my_gen))
