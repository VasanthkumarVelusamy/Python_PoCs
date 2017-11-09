emblem = {'Land':'PANDA','Water':'OCTOPUS','Ice':'MAMMOTH','Air':'OWL','Fire':'DRAGON'}
allies = []
ruler = None

def invite(kingdom):
    global message, allies

    for c in emblem[kingdom]:            # Gets the animal for the given kingdom and iterate through the charaters.
        found = False

        if i in message:
            message = message.replace(i,'',1)         # removes the first occurence of the charater matched with animal from the message.
            found = True
        if not found:
            return False

    allies.append(kingdom)
    return True

def allies_info():
    global allies, ruler

    if len(allies) == 0:
        _allies = None
    else:
        _allies = {x:y for (y, x) in enumerate(allies)}.keys()         # Adding the allies as keys in dictionary to avoid duplicates and also to keep insertion order.
        _allies = ', '.join(map(str,_allies))
    if len(_allies) >= 3:
        ruler = 'King Shan'

    print('Who is the ruler of Southeos?')
    print(ruler)
    print('Allies of King Shan?')
    print(_allies)

allies_info()
print('')
print('Input Messages to kingdoms from King Shan:')

while True:           # Reading input lines until getting an empty line.
    line = input()

    if line:
        try:
            kingdom, message = line.split(',')
            message = message.strip(' \"').upper()
            kingdom = kingdom.capitalize()
            invite(kingdom)
        except ValueError:
            print('Error: Invalid input!')
        except KeyError:
            print('Error: Invalid kingdom!')
    else:
        break

allies_info()
