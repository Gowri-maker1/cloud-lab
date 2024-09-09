def calculate_gpa(grades, credits):
    """Calculate GPA from grades and corresponding credit hours."""
    total_points = sum(grade * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    return total_points / total_credits if total_credits != 0 else 0

def main():
    print("Cumulative GPA Calculator")

    grades = []
    credits = []

    while True:
        try:
            grade = float(input("Enter grade (or -1 to finish): "))
            if grade == -1:
                break
            if grade < 0 or grade > 4.0:
                print("Invalid grade. Please enter a grade between 0 and 4.0.")
                continue

            credit = float(input("Enter credit hours for this course: "))
            if credit <= 0:
                print("Invalid credit hours. Please enter a positive number.")
                continue

            grades.append(grade)
            credits.append(credit)

        except ValueError:
            print("Invalid input. Please enter numerical values for grades and credits.")

    if grades and credits:
        gpa = calculate_gpa(grades, credits)
        print(f"Your cumulative GPA is: {gpa:.2f}")
    else:
        print("No grades were entered. GPA calculation could not be performed.")

if __name__ == "__main__":
    main()
