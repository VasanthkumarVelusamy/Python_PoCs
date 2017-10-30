class vehicle:
    def default_activity(self):
        print('transporting')

class car(vehicle):
    def specific_activity(self):
        print('luxury trip to goa')
class bike(vehicle):
    def specific_activity(self):
        print('awesome trip to goa')

r15 = bike()
r15.specific_activity()
