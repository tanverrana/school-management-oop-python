from School import School, ClassRoom
from Persons import Student


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
    print(school)


if __name__ == '__main__':
    main()
