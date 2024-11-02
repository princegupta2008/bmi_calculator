def calculate_bmi(weight, height):
    if height <= 0:
        return None, "Height must be greater than zero."
    height = height / 100
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "You are Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "You weight is Normal"
    elif 24.9 <= bmi < 29.9:
        category = "You are Overweight"
    else:
        category = "Obesity"

    return round(bmi, 2), category


def valid_input(value, value_name):
        try:
            value = float(value)
            if value <= 0:
                raise ValueError
            return value, None
        except ValueError:
            return None, f"Invalid {value_name}. Please enter a positive number."

def main():
    weight_input = input("Enter your weight (in kg): ")
    weight, error = valid_input(weight_input, "weight")
    if error:
        print(error)
        return

    height_input = input("Enter your height (in centimeters [cm]): ")
    height, error = valid_input(height_input, "height")
    if error:
        print(error)
        return

    bmi, category = calculate_bmi(weight, height)
    if bmi is not None:
        print(f"Your BMI is: {bmi} ({category})")
    else:
        print(category)

if __name__ == "__main__":
    main()