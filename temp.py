from flask import Flask, request, render_template_string

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

# HTML template as a string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Celsius to Fahrenheit Converter</title>
</head>
<body>
    <h1>Celsius to Fahrenheit Converter</h1>
    <form method="post">
        <label for="celsius">Temperature in Celsius:</label>
        <input type="text" id="celsius" name="celsius">
        <button type="submit">Convert</button>
    </form>
    
    {% if fahrenheit is not none %}
        <h2>Result:</h2>
        <p>
            {% if fahrenheit is string %}
                {{ fahrenheit }}
            {% else %}
                {{ request.form['celsius'] }}°C is equal to {{ fahrenheit|round(2) }}°F
            {% endif %}
        </p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    fahrenheit = None
    if request.method == 'POST':
        try:
            celsius = float(request.form['celsius'])
            fahrenheit = celsius_to_fahrenheit(celsius)
        except ValueError:
            fahrenheit = "Invalid input. Please enter a number."
    
    return render_template_string(HTML_TEMPLATE, fahrenheit=fahrenheit)

if __name__ == "__main__":
    app.run(debug=True)
