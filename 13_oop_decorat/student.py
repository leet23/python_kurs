import holidays, datetime

class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg


    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()


    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)


    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, average):
        cls.min_avg = average


obj_anna = Student('anna', 'kowalska', 23, 4.7)
obj_arek = Student('arkadiusz', 'nowak', 21, 3.9)
print(Student.min_avg)
print(obj_anna.min_avg)
print(obj_arek.min_avg)

obj_anna.set_min_avg(4.8)
print('Min srednia dla obiektu anna', obj_anna.min_avg)
print('Min srednia dla obiektu arek', obj_arek.min_avg)

