from view import AppWindow
from model import *
from controller import Controller


class Injector():

    def __init__(self):
        receptions = [Reception('Day ' + str(x), (x+8)%3) for x in range(7)]
        doctors = [Doctor('Name' + str(x), 'Surname'+ str(x), 'Speciality'+str(x), 'Category'+str(x), x, receptions) for x in range(10)] 
        hospitals = [Hospital('Name' +str(x),  'contact info', 'adress' + str(x), 'work time', doctors )for x in range(3)]
        profiles =[Profile('Name' + str(x), 'Surname'+ str(x), 'LOGIN', 'Email', 'PaSsWoRd', dict({doctors[x%len(doctors)]:receptions[x%len(receptions)]})) for x in range(10)]
        self.model = Model(doctors, hospitals, profiles)
        self.controller = Controller(self.model)
        self.view = AppWindow(self.controller)
    
    def run(self):
        self.view.run()

if __name__ == '__main__':
    Injector().run()

