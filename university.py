from typing import TextIO


def read_positive_integer() -> int:
    while True:
        try:
            number = int(input())
            if number < 0:
                raise ValueError()
            return number
        except ValueError:
            print("\nError: Your input must be an positive integer.\n")


def read_applicants_data() -> TextIO:
    with open('applicants.txt', mode='r', encoding="utf-8") as applicants_file:
        return applicants_file


departments = ('Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics')


def get_successful_applicants(data: dict, accepted_applicants: int):
    sorted_applicants = dict(
        sorted(data.items(), key=lambda item: (-item[1], item[0])))  # Sort by gpa(item[1]) then by name(item[0])
    successful_applicants = [item[0] for item in sorted_applicants.items()]
    return successful_applicants[:accepted_applicants]


def run() -> None:
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    read_applicants_data()
