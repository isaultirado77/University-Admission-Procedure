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

N = 5  # read_positive_integer()  # Number of applicants by department

accepted = defaultdict(list)


def sort_accepted_dict():
    for department, applicants in accepted.items():
        accepted[department] = list(sorted(applicants, key=lambda item: (-item[1], item[0])))


def get_successful_applicants():
    for department, applicants in accepted.items():
        accepted[department] = applicants[:N]


def delete_accepted_applicants_from_data():
    global applicants_data
    accepted_list = [item[1][i][0] for item in accepted.items() for i in range(5)]
    applicants_data = [applicant for applicant in applicants_data if f'{applicant.split()[0]} {applicant.split()[1]}' not in accepted_list]


def run_admission_procedure():
    for applicant in applicants_data:  # For each applicant
        name, surname, gpa, first, second, third = applicant.split()
        accepted[first].append((f'{name} {surname}', float(gpa)))

        # Sort by gpa then by name and surname
        sort_accepted_dict()

        # Get successful applicants given the total of applicants by department
        get_successful_applicants()

    # Delete accepted applicants
    delete_accepted_applicants_from_data()


def main() -> None:
    run_admission_procedure()


if __name__ == '__main__':
    main()
