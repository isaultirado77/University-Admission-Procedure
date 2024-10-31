def read_positive_integer() -> int:
    while True:
        try:
            number = int(input())
            if number < 0:
                raise ValueError()
            return number
        except ValueError:
            print("\nError: Your input must be an positive integer.\n")


def sort_dict_by_values(dictionary: dict = None, asc: bool = True) -> dict:
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=asc))


def read_applicants_data(applicants_number: int = 0) -> dict:
    data = {}
    for _ in range(applicants_number):
        split_line = input().split()
        full_name = f'{split_line[0]} {split_line[1]}'
        gpa = float(split_line[2])
        data[full_name] = gpa

    return data


def main():
    applicants = read_positive_integer()
    accepted_applicants = read_positive_integer()


if __name__ == '__main__':
    main()
