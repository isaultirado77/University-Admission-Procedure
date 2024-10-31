def read_grades() -> list:
    while True:
        try:
            grades = [float(input()) for _ in range(3)]
            return grades
        except ValueError:
            print("Error: Enter a number. ")


def calculate_mean_grade(grades: list = None) -> float:
    average = sum(grades) / len(grades)
    return average


def determine_status_admission(mean: float = 50.) -> str:
    if mean >= 60:
        return 'Congratulations, you are accepted!'
    else:
        return 'We regret to inform you that we will not be able to offer you admission.'


def main():
    grades = read_grades()
    mean = calculate_mean_grade(grades)
    print(mean)
    status_admission = determine_status_admission(mean)
    print(status_admission)


if __name__ == '__main__':
    main()
