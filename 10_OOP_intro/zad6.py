class Employee:
    company = "PythonTeam"

    def __init__(self, position, salary, name, surname, seniority, is_student):
        self.position = position
        self.salary = salary
        self.name = name
        self.seniority = seniority
        self.is_student = is_student

    def salary_bump(self):
        self.salary *= 1.20
        return self.salary

    def tax(self):
        return self.salary * 0.09

    def health_care(self):
        if self.is_student:
            return 0
        else:
            return self.salary * 0.8
    def employee_email(self):
        primary = self.name + '.' + self.surname
        secondary = self.company.strip().lower() + ".com"
        email = primary + "@" + secondary
        return email

p1 = Employee("Programista", 6000, "Stefan", "Kowalski", 3, False)
print(p1.salary)
print(p1.salary_bump())
print(p1.salary)

