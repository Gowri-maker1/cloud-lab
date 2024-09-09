from flask import Flask, request, render_template_string

app = Flask(__name__)

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
        return None
    
    total_grade_points = 0
    total_credits = 0
    
    for grade, credit in zip(grades, credits):
        total_grade_points += grade * credit
        total_credits += credit
    
    if total_credits == 0:
        return 0
    
    return total_grade_points / total_credits

# HTML template as a string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGPA Calculator</title>
</head>
<body>
    <h1>CGPA Calculator</h1>
    <form method="post">
        <div id="courses">
            <div class="course">
                <label for="grade1">Grade for course 1:</label>
                <input type="text" id="grade1" name="grades" required>
                <label for="credit1">Credit hours for course 1:</label>
                <input type="text" id="credit1" name="credits" required>
            </div>
        </div>
        <button type="button" onclick="addCourse()">Add More Courses</button>
        <button type="submit">Calculate CGPA</button>
    </form>
    
    {% if cgpa is not none %}
        <h2>Result:</h2>
        <p>Your CGPA is: {{ cgpa|round(2) }}</p>
    {% endif %}
    
    <script>
        let courseCount = 1;

        function addCourse() {
            courseCount++;
            const courseDiv = document.createElement('div');
            courseDiv.classList.add('course');
            courseDiv.innerHTML = `
                <label for="grade${courseCount}">Grade for course ${courseCount}:</label>
                <input type="text" id="grade${courseCount}" name="grades" required>
                <label for="credit${courseCount}">Credit hours for course ${courseCount}:</label>
                <input type="text" id="credit${courseCount}" name="credits" required>
            `;
            document.getElementById('courses').appendChild(courseDiv);
        }
    </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    cgpa = None
    if request.method == 'POST':
        try:
            grades = list(map(float, request.form.getlist('grades')))
            credits = list(map(int, request.form.getlist('credits')))
            cgpa = calculate_cgpa(grades, credits)
        except ValueError:
            cgpa = "Invalid input. Please enter valid numbers for grades and credits."
    
    return render_template_string(HTML_TEMPLATE, cgpa=cgpa)

if __name__ == "__main__":
    app.run(debug=True)
