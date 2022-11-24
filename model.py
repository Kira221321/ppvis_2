from typing import Dict, List


class Reception(): 
    def __init__(self, day: str, time : int):
        self.day = day
        self.time = time

    def __str__(self):
        return self.day + ':' + str(self.time)

class Doctor():
    def __init__(self, name: str, last_name: str, speciality: str, category: str, room: int, reception_time: List[Reception]):
        self.name = name
        self.last_name = last_name
        self.speciality = speciality
        self.category = category
        self.room = room
        self.reception_time = reception_time

class Profile():
    def __init__(self, name: str, last_name: str, login: str, mail: str, password: str, history_of_visit: Dict[Doctor, Reception]):
        self.name = name
        self.last_name = last_name
        self.login = login
        self.mail = mail
        self.password = password
        self.history_of_visit = history_of_visit

    def Exit():
        pass

    def EditInfo():
        pass

class Hospital():
    def __init__(self, name: str, contact_info: str, adress: str, work_time: str, doctor: List[Doctor]):
        self.name = name
        self.contact_info = contact_info
        self.adress = adress
        self.work_time = work_time
        self.doctor = doctor  


class Model():
    def __init__(self, list_doctor: List[Doctor], list_hospital: List[Hospital], profile: List[Profile]):
        self.list_doctor = list_doctor
        self.list_hospital = list_hospital
        self.profile = profile

    def Registration():
        pass

    def Enter():
        pass

    def ResetPassword():
        pass

    def FindHospital(hospital : Hospital):
        pass

    def FindDoctor(doctor: Doctor):
        pass

    def ShowHospital():
        pass
    
    def ShowDoctor():
        pass

    def MakeAppointment():
        pass

    def ShowVisitHistory(profile: Profile):
        pass
