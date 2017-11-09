
def count_substring(string,sub_string):
    index = string.find(sub_string)
    if index >=0:
        count += 1
        count_substring(string[index+1:],sub_string)

    return count
count =0
string = input().strip()
sub_string = input().strip()

count = count_substring(string,sub_string)
print(count)
