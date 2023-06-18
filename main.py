from School import School, ClassRoom, Subject
from Persons import Student, Teacher


def main():
    school = School('Tanver', 'Mohammadpur')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add students
    tamim = Student('Tamim Iqbal', eight)
    school.student_admission(tamim)
    shakib = Student('Shakib Al Hasan', eight)
    school.student_admission(shakib)
    mushi = Student('Mushfiqur Rahim', eight)
    school.student_admission(mushi)

    # subjects
    physics_teacher = Teacher('Haturu singh')
    physics = Subject('physics', physics_teacher)
    eight.add_subject(physics)

    chemestry_teacher = Teacher('Anal Donald')
    chemestry = Subject('chemestry', chemestry_teacher)
    eight.add_subject(chemestry)

    biology_teacher = Teacher('Thompash')
    biology = Subject('biology', biology_teacher)
    eight.add_subject(biology)

    print(school)


if __name__ == '__main__':
    main()
