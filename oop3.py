class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = f'Имя:{self.name}\nФамилия:{self.surname}'
        if len(self.grades) != 0:
            student_grades = f'Средняя оценка за домашние задания:{sum(self.grades) / len(self.grades)} '
        else:
            student_grades = 0
        print(some_student)
        print(student_grades)
        print(f'Курсы в процессе изучения:{self.courses_in_progress}')
        print(f'Завершенные курсы:{self.finished_courses}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
        return self.grades < other.grades
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        some_lecturer = f'Имя:{self.name}\nФамилия:{self.surname}'
        if len(self.grades) != 0:
            lecturer_grades = f'Средняя оценка за лекции:{sum(self.grades) / len(self.grades)} '
        else:
            lecturer_grades = 0
        print(some_lecturer)
        print(lecturer_grades)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade = {}

    def __str__(self):
        some_lecturer = f'Имя:{self.name}\nФамилия:{self.surname}'
        #lecturer_grades = f'Средняя оценка за лекции:{sum(self.grades) / len(self.grades)} '
        print(some_lecturer)
        #print(lecturer_grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
        return self.grades < other.grades


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя:{self.name}\nФамилия:{self.surname} '

        print(some_reviewer)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
student_one = Student('Alex', 'Leo','male')
student_one.courses_in_progress += ['Java']



reviewer_one = Reviewer('Olga', 'Dark')
reviewer_one.__str__()
reviewer_two = Reviewer('Oleg', 'Dark')
reviewer_two.__str__()
reviewer_one.rate_hw(best_student, 'Python', 10)
reviewer_one.rate_hw(student_one, 'Python', 7)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
mentor_two = Mentor ('Bob', 'Doll')

lecturer_one = Lecturer('Summer', 'Winter')
lecturer_two = Lecturer('Sam', 'Winter')

cool_mentor.__str__()
mentor_two.__str__()
best_student.__str__()
student_one.__str__()
lecturer_one.__str__()
lecturer_two.__lt__(lecturer_two, lecturer_one)
student_one.rate_lc(lecturer_one, 'Java', 9)
best_student.rate_lc(lecturer_two, 'Python', 5)