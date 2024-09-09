def calculate_cgpa(grades, credits):
    """
    Calculate the CGPA given a list of grades and their corresponding credit hours.
    
    Parameters:
    grades (list of float): List of grades received in each course.
    credits (list of int): List of credit hours for each course.
    
    Returns:
    float: The calculated CGPA.
    """
    if len(grades) != len(credits) or not grades or not credits:
        raise ValueError("Grades and credits lists must be of the same length and cannot be empty.")
    
    total_grade_points = 0
    total_credits = 0
    
    for grade, credit in zip(grades, credits):
        total_grade_points += grade * credit
        total_credits += credit
    
    if total_credits == 0:
        return 0
    
    return total_grade_points / total_credits

def main():
    try:
        num_courses = int(input("Enter the number of courses: "))
        
        if num_courses <= 0:
            print("The number of courses should be greater than zero.")
            return
        
        grades = []
        credits = []
        
        for i in range(num_courses):
            grade = float(input(f"Enter grade for course {i+1}: "))
            credit = int(input(f"Enter credit hours for course {i+1}: "))
            
            if grade < 0 or credit <= 0:
                print("Grade should be non-negative and credit hours should be positive.")
                return
            
            grades.append(grade)
            credits.append(credit)
        
        cgpa = calculate_cgpa(grades, credits)
        print(f"Your CGPA is: {cgpa:.2f}")
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
