def print_two(*args):
    arg1, arg2 = args
    print("I got the items {} {}".format(arg1,arg2))

def print_two_again(arg1, arg2):
    print(f"I now got two items again, {arg1}, {arg2}")

def print_one(arg1):
    print(f"now i got only one, {arg1}")

def print_none():
    print("i got none this time")

print_two("vasanth","divi")
print_two_again("vasanth", "kumar")
print_one("divi")
print_none()
