class Applicant:
    def __init__(self, name: str, scores: tuple, priorities: tuple):
        self.name = name
        self.scores = scores
        self.priorities = priorities

    def __str__(self):
        return f'{self.name} {self.scores} {self.priorities}'

    def get_score(self, subjet_name: str):
        indices = {'physics': 0, 'chemistry': 1, 'math': 2, 'computer science': 3}
        index = indices[subjet_name]
        return self.scores[index]


class Department:
    def __init__(self, name: str, required_skill: str):
        self.name = name
        self.accepted_students = list()
        self.required_skills = required_skill

    def __str__(self):
        text = list()
        for student in sorted(self.accepted_students, key=lambda x: (-x.get_score(self.required_skills), x.name)):
            text.append(f'{student.name} {student.get_score(self.required_skills)}')
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
    with open('applicants.txt', mode='r', encoding="utf-8") as file:
        for line in file:
            data = line.split()
            name = f'{data[0]} {data[1]}'
            scores = (float(data[2]), float(data[3]), float(data[4]), float(data[5]))
            priorities = (data[6], data[7], data[8])
            applicants.append(Applicant(name, scores, priorities))
        return applicants


class University:
    def __init__(self):
        self.departments = self.create_departments()
        self.start_admission_procedure()
        self.display_department_students()

    @staticmethod
    def create_departments():
        departs = list()
        departs.append(Department('Biotech', 'chemistry'))
        departs.append(Department('Chemistry', 'chemistry'))
        departs.append(Department('Engineering', 'computer science'))
        departs.append(Department('Mathematics', 'math'))
        departs.append(Department('Physics', 'physics'))
        return departs

    def start_admission_procedure(self):
        naccepted = read_positive_integer()
        applicants = read_applicants_data()
        for i in range(0, 3):
            for department in self.departments:
                remaining = sorted(applicants, key=lambda x: (-x.get_score(department.required_skills), x.name))
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
    University()


if __name__ == '__main__':
    main()
