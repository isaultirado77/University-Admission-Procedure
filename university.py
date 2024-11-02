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

N = read_positive_integer()  # Number of applicants by department

accepted = defaultdict(list)


def sort_accepted_dict():
    for department, applicants in accepted.items():
        accepted[department] = list(sorted(applicants, key=lambda item: (-item[1], item[0])))


def get_successful_applicants():
    for department, applicants in accepted.items():
        accepted[department] = applicants[:N]


def delete_accepted_applicants_from_data():
    global applicants_data
    accepted_list = [item[0] for department in accepted.values() for item in department]
    applicants_data = [applicant for applicant in applicants_data if
                       f'{applicant.split()[0]} {applicant.split()[1]}' not in accepted_list]


def run_admission_procedure():
    for priority in range(3, 6):  # For each applicant priority
        for applicant in applicants_data:  # For each applicant
            data = applicant.split()
            name = f'{data[0]} {data[1]}'
            gpa = float(data[2])
            department_choice = data[priority]

            # Add applicant to the chosen department
            accepted[department_choice].append((name, gpa))

        # Sort by gpa then by name and surname
        sort_accepted_dict()

        # Keep only the successful applicants
        get_successful_applicants()

        # Remove accepted applicants from the main data
        delete_accepted_applicants_from_data()


def display_accepted_applicants():
    departments = ('Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics')
    for department in departments:
        print(department)

        for accepted_applicant in accepted[department]:
            print(f'{accepted_applicant[0]} {accepted_applicant[1]}')

        print()


def main() -> None:
    run_admission_procedure()
    display_accepted_applicants()


if __name__ == '__main__':
    main()
