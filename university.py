def read_positive_integer() -> int:
    while True:
        try:
            number = int(input())
            if number < 0:
                raise ValueError()
            return number
        except ValueError:
            print("\nError: Your input must be an positive integer.\n")


def read_applicants_data(applicants_number: int = 0) -> dict:
    data = {}
    for _ in range(applicants_number):
        split_line = input().split()
        full_name = f'{split_line[0]} {split_line[1]}'
        gpa = round(float(split_line[2]))
        data[full_name] = gpa

    return data


def get_successful_applicants(data: dict, total_applicants: int):
    sorted_applicants = dict(sorted(data.items(), key=lambda item: (item[1], item[0])),
                             reverse=True)  # Sort by gpa(item[1]) then by name(item[0])
    successful_applicants = [item[0] for item in sorted_applicants.items()]
    return successful_applicants[:total_applicants]


def main():
    total_applicants = read_positive_integer()
    total_accepted_applicants = read_positive_integer()
    applicants_data = read_applicants_data(total_applicants)
    successful_applicants = get_successful_applicants(applicants_data, total_accepted_applicants)
    for applicant in successful_applicants:
        print(applicant)


if __name__ == '__main__':
    main()
