# Tame of Thrones!
emblem = {'Land':'PANDA','Water':'OCTOPUS','Ice':'MAMMOTH','Air':'OWL','Fire':'DRAGON'}
allies = []
ruler = None

# Function to invite kingdom with message.
def invite(kingdom, message):
    global allies

    for c in emblem[kingdom]:            # Gets the animal for the given kingdom and iterate through the charaters.
        if c in message:               # Checks if the character is present in the message.
            message = message.replace(c,'',1)         # removes the first occurence of the charater matched.
        else:
            return
    allies.append(kingdom)          # Allies that have accepted the invitation are appended to the list.

# Function to print Ruler and Allies information.
def allies_info():
    global allies, ruler
    unique_allies = {x:y for (y, x) in enumerate(allies)}.keys()      # Adding the allies as keys in dictionary to avoid duplicates and also to keep insertion order.
    allies_string = ', '.join(map(str,unique_allies))        # String to print allies.

    if len(unique_allies) == 0:
        allies_string = None
    elif len(unique_allies) >= 3:           # Electing the ruler if he gets 3 or more allies.
        ruler = 'King Shan'

    print('Who is the ruler of Southeros?')
    print(ruler)
    print('Allies of King Shan?')
    print(allies_string)

# Function to get message and invite kingdom.
def get_message_and_invite():
    while True:           # Reading input lines until getting an empty line.
        line = input()

        if line:
            try:
                kingdom, message = line.split(',')
                message = message.strip(' \"').upper()
                kingdom = kingdom.capitalize()
                invite(kingdom,message)        # Invite kingdom with message.
            except ValueError:
                print('Error: Invalid input!')
            except KeyError:
                print('Error: Invalid kingdom!')
        else:
            break

# Main program flow
allies_info()
print('')
print('Input Messages to kingdoms from King Shan:')
get_message_and_invite()
allies_info()
