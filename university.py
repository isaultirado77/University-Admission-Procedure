class Applicant:
    def __init__(self, name: str, scores: tuple, priorities: tuple):
        self.name = name
        self.scores = scores
        self.priorities = priorities

    def __str__(self):
        return f'{self.name} {self.scores} {self.priorities}'

    def get_mean_score(self, subjet_names: tuple) -> float:
        indices = {'physics': 0, 'chemistry': 1, 'math': 2, 'computer science': 3}
        summ = 0
        for name in subjet_names:
            index = indices[name]
            summ += self.scores[index]
        return round(summ / len(subjet_names), 1)


class Department:
    def __init__(self, name: str, required_skills: tuple):
        self.name = name
        self.accepted_students = list()
        self.required_skills = required_skills

    def __str__(self):
        text = list()
        for student in sorted(self.accepted_students, key=lambda x: (-x.get_mean_score(self.required_skills), x.name)):
            text.append(f'{student.name} {student.get_mean_score(self.required_skills)}')
        text.append('')
        return '\n'.join(text)

    @property
    def nstudents(self) -> int:
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
    with open('applicant_list.txt', mode='r', encoding="utf-8") as file:
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
        self.generate_output_files()

    @staticmethod
    def create_departments() -> list:
        departs = list()
        departs.append(Department('Biotech', ('chemistry', 'physics')))
        departs.append(Department('Chemistry', ('chemistry',)))
        departs.append(Department('Engineering', ('computer science', 'math')))
        departs.append(Department('Mathematics', ('math',)))
        departs.append(Department('Physics', ('physics', 'math')))
        return departs

    def start_admission_procedure(self) -> None:
        naccepted = read_positive_integer()
        applicants = read_applicants_data()
        for i in range(0, 3):
            for department in self.departments:
                remaining = sorted(applicants, key=lambda x: (-x.get_mean_score(department.required_skills), x.name))
                for applicant in remaining:
                    if department.nstudents == naccepted:
                        break
                    if applicant.priorities[i] == department.name:
                        department.accepted_students.append(applicant)
                        applicants.remove(applicant)

    def display_department_students(self) -> None:
        for department in self.departments:
            print(department.name)
            print(department)

    def generate_output_files(self) -> None:
        for department in self.departments:
            filename = department.name.lower() + '.txt'
            with open(filename, 'w') as file:
                file.write(department.__str__())


def main() -> None:
    University()


if __name__ == '__main__':
    main()
