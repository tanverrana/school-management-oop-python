class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = []
        # composition
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            # todo: set student id, (roll num) at the time of adding the student
            self.classrooms[className].add_student(student)
        else:
            print(f'No classroom as named{className}')

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks <= 70:
            return 'A-'
        elif 50 <= marks <= 60:
            return 'B'
        elif 40 <= marks <= 50:
            return 'C'
        elif 33 <= marks <= 40:
            return 'D'
        else:
            return 'F'

    def __repr__(self) -> str:
        print('---------All Classroom----------')
        for key, value in self.classrooms.items():
            print(key)

        print('--------------Students------------')
        eight = self.classrooms['eight']
        print('Number of sutdents for class Eight:', len(eight.students))
        for student in eight.students:
            print(student.name)

        print('-------------Subjects---------------')
        for subject in eight.subjects:
            print('Subject name: ', subject.name, '--->',
                  'Teacher Name: ', subject.teacher.name)

        print('------------Student Exam Marks------------')
        for student in eight.students:
            for key, value in student.marks.items():
                print(student.name, key, value, student.subject_grade[key])
            print('_______End Student___________')

        return ''


class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        # composition
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students)+1}'
        student.id = serial_id
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'

    # todo: sort students by grade
    def get_top_students(self):
        pass


class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 30

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)
