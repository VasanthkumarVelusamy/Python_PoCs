 # V  A  S  A  N  T  H


 # B  A  N  A  N  A

def minion_game(string):

    Stuart = 0
    Kevin = 0
    vowels = ['A','E','I','O','U']
    for index, c in enumerate(string):
        i=index+1
        if c in vowels:
            for _ in string[index:]:
                Kevin += 1
                i += 1
        if c not in vowels:
            for _ in string[index:]:
                Stuart += 1
                i += 1
    if Kevin > Stuart:
        print('Kevin '+str(Kevin))
    elif Kevin < Stuart:
        print('Stuart '+str(Stuart))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)


######################################################


s = raw_input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"
