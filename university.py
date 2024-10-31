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


def main():
    grades = read_grades()
    mean = calculate_mean_grade(grades)
    print(mean)
    print('Congratulations, you are accepted!')



if __name__ == '__main__':
    main()
