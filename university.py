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
        self.accepted_students = []

    def __str__(self):
        text = list()
        for student in sorted(self.accepted_students, key=lambda x: (-x.gpa, x.name)):
            text.append(f'{student.name} {student.gpa}')
        text.append('')
        return '\n'.join(text)

    @property
    def nstudents(self):
        return len(self.accepted_students)


def main() -> None:
    pass


if __name__ == '__main__':
    main()
