def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def main():
    try:
        # Get user input
        celsius = float(input("Enter temperature in Celsius: "))
        
        # Calculate Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        
        # Display the result
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    except ValueError:
        print("Please enter a valid number for the temperature.")

if __name__ == "__main__":
    main()
