def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) using weight (in kilograms) and height (in meters).

    Args:
        weight_kg (float): Weight of the person in kilograms.
        height_m (float): Height of the person in meters.

    Returns:
        float: Calculated BMI value.
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value and provide a corresponding category.

    Args:
        bmi (float): Calculated BMI value.

    Returns:
        str: The interpretation category of BMI.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid input. Weight and height must be positive numbers.")
        else:
            bmi_value = calculate_bmi(weight, height)
            bmi_category = interpret_bmi(bmi_value)

            print(f"Your BMI is: {bmi_value:.2f}")
            print(f"Interpretation: {bmi_category}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for weight and height.")
