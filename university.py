from collections import defaultdict


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
    with open('applicants.txt', mode='r', encoding="utf-8") as applicants_file:
        return applicants_file.read().splitlines()


applicants_data = read_applicants_data()
departments = ('Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics')

N = read_applicants_data()  # Number of applicants by department

accepted = defaultdict(list)


def sort_accepted_dict():
    for department, applicants in accepted.items():
        print(department, applicants)
        accepted[department] = list(sorted(applicants, key=lambda item: (-item[1], item[0])))


def get_successful_applicants_by_department():
    for applicant in applicants_data:  # For each applicant
        name, surname, gpa, first, second, third = applicant.split()
        accepted[first].append((f'{name} {surname}', float(gpa)))
        # Sort by gpa then by name and surname
        sort_accepted_dict()


def main() -> None:
    get_successful_applicants_by_department()


if __name__ == '__main__':
    get_successful_applicants_by_department()
