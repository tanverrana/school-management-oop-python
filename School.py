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

    def student_admission(self, student, classroom_name):
        if classroom_name in self.classrooms:
            # todo: set student id, (roll num) at the time of adding the student
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f'No classroom as named{classroom_name}')


class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        # composition
        self.students = []

    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students)+1}'
        student.id = serial_id
        self.students.append(student)

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'

    # todo: sort students by grade
    def get_top_students(self):
        pass
