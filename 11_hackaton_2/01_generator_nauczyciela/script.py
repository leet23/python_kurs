import csv

def open_csv_file(file):
    with open(file + '.csv', 'r') as f:
        reader = csv.reader(f)
        students = list(reader)
    return students

def create_students_dict(lista):
    # print(lista)
    students = {}
    for i in lista:
        students[i[0] + i[1] + i[2]] = [i[1], i[2], i[3], i[4]]
    return students

def search_name(name, students):
    lista = []
    for k, v in students.items():
        if name in k:
            lista.append(v)
    return lista

def search_grade(grade, students):
    lista = []
    for k, v in students.items():
        if v[3] == grade:
            lista.append(v)
    return lista

def search_task(task, students):
    lista = []
    for k, v in students.items():
        if v[2] == task:
            lista.append(v)
    return lista

def create_message(length):
    with open('messages.csv', 'r', encoding='utf-8') as f:
        reader1 = csv.reader(f)
        txt = list(reader1)
    # print(txt)
    message = []
    while length > 0:
        print("treść nowej wiadomości", message)

        for i in range(len(txt)):
            print(i, ''.join(txt[i]))
        wybierz = int(input("treśc wiadomośći"))
        message.append(''.join(txt[wybierz]))
        length -= 1
    return ', '.join(message)

def send_message(students, message):
    names = []
    tasks = []
    grades = []
    for i in students:
        names.append(i[0])
        tasks.append(i[2])
        grades.append(i[3])

    for name, task, grade in zip(names, tasks, grades):
        print(message.format(name, task, grade, int(grade) + 1))

message_txt = "Hi {},\n\nThis is a reminder that you have {} tasks left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
files = ['3a', '3b', '3c', '3d']
for i in files:
    print("We have class:", i)
file1 = input("Select class:")
open_class_file = open_csv_file(file1)
students_list = create_students_dict(open_class_file)
print('***** 1 - Search by name  *****'
            '\n***** 2 - Search by grade  *****'
            '\n***** 3 - Search by number of tasks  *****'
            '\n***** 4 - Exit  *****')
your_choice = input("").lower()
if your_choice == '1':
    new_name = input("Give name: \n")
    a = search_name(new_name, students_list)
if your_choice == '2':
    new_grade = input("Give grade: \n")
    a = search_grade(new_grade, students_list)
if your_choice == '3':
    new_task = input("Give number of task: \n")
    a = search_task(new_task, students_list)
if your_choice == '4':
    exit()
send_message(a, message_txt)


# send_message(students_new, message_txt)

