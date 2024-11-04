class Applicant:
    def __init__(self, name: str, gpa: float, priorities: tuple):
        self.name = name
        self.gpa = gpa
        self.priorities = priorities

    def __str__(self):
        return f'{self.name} {self.gpa} {self.priorities}'


class Department:
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
