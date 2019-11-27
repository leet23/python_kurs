import datetime

class Zegarek():
    def __init__(self):
        print("zegarek")

    def current_time(self):
        return datetime.datetime.now().time()

class Kalendarz():
    def __init__(self):
        pass
    def current_date(self):
        return datetime.datetime.now().date()

class ZegarkoKalendarz(Zegarek, Kalendarz):
    def  current_date_time(self):
        print(super().current_date())
        print(super().current_time())

zk=ZegarkoKalendarz()
zk.current_date_time()

print(zk.current_time())