  def __init__(self, name, last, age):
    self.name = name
    self.last = last
    self.age = age
    self.email = name + '.' + last + '@university.com'


  def __repr__(self):
    return f'Student: {self.name.capitalize()} {self.last.capitalize()}'


obj_anna = Student('ana', 'kowalska', 23)
print(obj_anna)
print(obj_anna.email)