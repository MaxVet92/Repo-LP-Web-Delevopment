
# feedback 20260216: as mentioned, all imports always on top of the file, so move the import re to the top.
def get_name() -> str:
    # Get the user's name
    # Accept capital letters, small letters, accents, hyphens, aposthophes
    pattern = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[ '\-][A-Za-zÀ-ÖØ-öø-ÿ]+)*$")

    while True:
        name = input("Enter your name: ")
        if pattern.fullmatch(name):
            return name
        print("Input not valid. Please try again")

def get_weight_unit() -> str:
# Ask the user which weight unit they want
    while True:
        unit = input("Choose between pounds and kg as your weight input unit: ")
        if unit in ("pounds", "kg"):
            return unit
        print("Wrong input. Please try again")

def get_weight(name: str, weight_unit: str) -> float:
    # Ask the user for weight and convert to kg if needed
    while True:
        try:
            weight_input = float(input(f"Hello, {name}. Please enter your weight in {weight_unit}: "))
            weight = weight_input if weight_unit == "kg" else weight_input * 0.453592

            if weight <= 0:
                print("Your weight must be greater than 0")
            elif weight <= 20:
                print("Your weight input must be realistic. Please enter again")
            else:
                return weight
        except ValueError:
            print("Please type a valid number")

def get_height_unit() -> str:
    # Ask the user which height unit they want
    while True:
        unit = input("Choose between inches and cm as your height input unit: ")
        if unit in ("inches", "cm"):
            return unit
        print("Wrong input. Please try again")

def get_height(height_unit: str) -> float:
    # Ask the user for height and convert to meters
    while True:
        try:
            height_input = float(input(f"Great, now please enter your height in {height_unit}: "))
            height = height_input * 0.01 if height_unit == "cm" else height_input * 0.0254

            if height <= 0:
                print("Invalid height. Please try again.")
            else:
                return height
        except ValueError:
            print("You didn't type in a number. Please try again.")

def get_info() -> tuple[str, float, float]:
    # Main function to get all info
    name = get_name()
    weight_unit = get_weight_unit()
    weight = get_weight(name, weight_unit)
    height_unit = get_height_unit()
    height = get_height(height_unit)
    return name, weight, height
    
def get_bmi(weight: float, height: float) -> float:    
    # calculate the BMI
    """Calculate the Body-Mass-Index (BMI).
     
    Parameters:
    weight (float): weight in kilogram (kg)
    height (float): height in centimeters (m) 
    
    Return:
    float: BMI value
    """
    return weight / height ** 2

def get_bmi_category(bmi: float) -> str:
    # Calculate BMI category
    if bmi < 18.5:
        category = "Underweight"

    elif bmi <= 24.9:
        category = "Normal weight"

    elif bmi <= 29.9:
        category = "Overweight"

    else:
        category = "Obese"
    return category

# Main, function calling
if __name__ == "__main__":
    import re
    name, weight, height = get_info()
    bmi: float = get_bmi(weight, height)
    category: str = get_bmi_category(bmi)

    # Closing message
    if name in ("Ksenia","ksenia", "Tim","tim", "Mo","mo"):
        print(f"Your BMI is {bmi}, but you´re fat anyways, says Ksenia")

    else:
        print(f"{name}, your BMI is: {bmi}. Your weight category therefore is: {category}.")
        if category == "Underweight":
            print("you are too weak. Eat more!")
        elif category == "Normal weight":
            print("You are great. Continue like that")
        elif category == "Overweight":
            print("You are too fat, do more sports and eat less!")
        else:
            print("You are way too big. You need to change your lifestyle")