class Applicant:
    def __init__(self, name: str, gpa: float, priorities: tuple):
        self.name = name
        self.gpa = gpa
        self.priorities = priorities

    def __str__(self):
        return f'{self.name} {self.gpa} {self.priorities}'


class Department:
    def __init__(self, name: str):
        self.name = name
        self.accepted_students = list()

    def __str__(self):
        text = list()
        for student in sorted(self.accepted_students, key=lambda x: (-x.gpa, x.name)):
            text.append(f'{student.name} {student.gpa}')
        text.append('')
        return '\n'.join(text)

    @property
    def nstudents(self):
        return len(self.accepted_students)


def read_positive_integer() -> int:
    while True:
        try:
            number = int(input())
            if number < 0:
                raise ValueError()
            return number
        except ValueError:
            print("\nError: Your input must be an positive integer.\n")


def read_applicants_data() -> list:
    applicants = list()
    # with open('applicants.txt', mode='r', encoding="utf-8") as file:
    with open('applicant_list.txt', mode='r', encoding="utf-8") as file:  # For testing
        for line in file:
            data = line.split()
            applicants.append(Applicant(f'{data[0]} {data[1]}', float(data[2]), (data[3], data[4], data[5])))
        return applicants


class University:
    def __init__(self):
        self.departments = self.create_departments()
        self.start_admission_procedure()
        self.display_department_students()

    @staticmethod
    def create_departments():
        departs = list()
        departs.append(Department('Biotech'))
        departs.append(Department('Chemistry'))
        departs.append(Department('Engineering'))
        departs.append(Department('Mathematics'))
        departs.append(Department('Physics'))
        return departs

    def start_admission_procedure(self):
        naccepted = read_positive_integer()
        applicants = read_applicants_data()
        for i in range(0, 3):
            for department in self.departments:
                remaining = sorted(applicants, key=lambda x: (-x.gpa, x.name))
                for applicant in remaining:
                    if department.nstudents == naccepted:
                        break
                    if applicant.priorities[i] == department.name:
                        department.accepted_students.append(applicant)
                        applicants.remove(applicant)

    def display_department_students(self):
        for department in self.departments:
            print(department.name)
            print(department)


def main() -> None:
    pass


if __name__ == '__main__':
    main()
