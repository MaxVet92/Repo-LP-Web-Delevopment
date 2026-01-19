
# Inquire name, height and weight of the user
def get_info() -> tuple[str, float, float]:
    """
    Let the user input values for their name, weight and height.
     
    Parameters:
    None
    
    Return:
    string: name
    float: weight
    float: height
    """
    # enter name
    while True:
        name = input("Enter your name: ")
        if name != "" and name.isalpha():
            break
        print("Input not valid. Please try again")

    # Choose weight unit
    def weight_unit() -> str:
        while True:
            weight_unit: str = input("Choose between pounds and kg as your weight input unit ")
            if weight_unit in ("pounds", "kg"):
                break
            print("Wrong input. Please try again")
        return weight_unit
    
    weight_unit: str = weight_unit()

    # enter weight
    while True:
        try:
            if weight_unit == "kg":
                weight = float(input(f"Hello, {name}. Please enter your weight in {weight_unit} "))
            else:
                weight = float(input(f"Hello, {name}. Please enter your weight in {weight_unit} ")) * 0.453592
            if weight <= 0:
                print("Your weigt must be greater than 0")
                continue
            elif weight <= 20:
                print("Your weigt input must be realistic. Please enter again")
                continue
            break
        except ValueError:
            print("Please type a valid number")
        
# Choose height unit
    def height_unit() -> str:
        while True:
            height_unit: str = input("Choose between inches and cm as your height input unit ")
            if height_unit in ("inches", "cm"):
                break
            print("Wrong input. Please try again")
        return height_unit
    
    height_unit: str = height_unit()

    # enter height
    while True:
        try:
            if height_unit == "cm":
                height = float(input(f"Great, now please enter your height in {height_unit} ")) * 0.01
            else:
                height = float(input(f"Great, now please enter your height in {height_unit} ")) * 0.0254
                if height <= 0:
                    print("Invalid height. Please try again.")
                    continue
            break
        except ValueError:
            print("You didn't type in a number please try again")
        print(height)
    return name, weight, height
    
# calculate the BMI
def BMI(weight: float, height: float) -> tuple[float, float]:
    """Calculate the Body-Mass-Index (BMI).
     
    Parameters:
    weight (float): weight in kilogram (kg)
    height (float): height in centimeters (cm) 
    
    Return:
    float: BMI vlaue
    """
    return weight / height ** 2


# Variable definitions
name, weight, height = get_info()

bmi: float = BMI(weight, height)


# Calculate BMI category
def get_bmi_category(bmi: float) -> str:
    
    if bmi < 18.5:
        Category = "Underweight"

    elif bmi <= 24.9:
        Category = "Normal weight"

    elif bmi <= 29.9:
        Category = "Overweight"

    else:
        Category = "Obese"
    return Category

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
    elif category == "overweight":
        print("You are too fat, do more sports and eat less!")
    else:
        print("You are way too fat. You need to change your life drastically")