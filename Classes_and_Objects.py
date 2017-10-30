class Human:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == 'playing tennis':
            print('Plays tennis')
        if self.occupation == 'shoots movies':
            print('Shooting films')

    def speak(self):
        print(self.name, 'says "How are you"')


tom = Human('Tom Cruise','shoots movies')
tom.do_work()
tom.speak()

maria = Human('Maria Sharapova', 'playing tennis')
maria.do_work()
maria.speak()
