# Exceptions

val1 = input('Enter divident ')
val2 = input('Enter Divisor ')
try:
    result = int(val1)/int(val2)
except Exception as e:
    print('Got an exception called ', e)
    result = None

print('The result is ',result)
