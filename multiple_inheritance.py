class father:
    def skills(self):
        print('Programming')

class mother:
    def skills(self):
        print('Cooking')

class son(mother,father):
    def skills(self):
        father.skills(self)


vid = son()
vid.skills()
