S = input()
str_list = [char.isalnum() for char in S]
print(str_list)

print(any(str_list))
print(any([char.isalnum() for char in S]))

# print any(str_list)
# print any([char.isalpha() for char in S])
# print any([char.isdigit() for char in S])
# print any([char.islower() for char in S])
# print any([char.isupper() for char in S])
