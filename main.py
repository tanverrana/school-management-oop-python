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

    tamim = Student('Tamim Iqbal', eight)
    school.student_admission(tamim)
    print(school)


if __name__ == '__main__':
    main()
