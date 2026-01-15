
### Inquire name, height and weight of the user
def get_info():
    """
    Let the user input values for their name, weight and height.
     
    Parameters:
    None
    
    Return:
    string: name
    float: weight
    float: height
    """
    ## enter name
    while True:
        name = input("Enter your name:")
        if name != "" and name.isalpha():
            break
        print("Input not valid. Please try again")

    ## enter weight
    while True:
        try:
            weight = float(input("Hello, " + name + ". Please enter your weight in Kg"))
            if weight <= 0:
                print("Your weigt must be greater than 0")
                continue
            break
        except ValueError:
            print("Please type a valid number")
        

    ## enter height
    while True:
        try:
            height = float(input("Great, now please enter your height in cm")) / 100
            if height <= 0:
                print("Invalid height. Please try again.")
                continue
            break
        except:
            ValueError
            print("You didn't type in a number please try again")
    return name, weight, height


### calculate the BMI
def BMI(weight, height):
    """Calculate the Body-Mass-Index (BMI).
     
    Parameters:
    weight (float): weight in kilogram (kg)
    height (float): height in centimeters (cm) 
    
    Return:
    float: BMI vlaue
    """
    return weight / height**2

### Variable definitions
name, weight, height = get_info()

BMI = round(BMI(weight, height), 2)

### Calculate BMI category
def BMI_cat(BMI):
    
    if BMI < 18.5:
        Category = "Underweight"

    elif BMI <= 24.9:
        Category = "Normal weight"

    elif BMI <= 29.9:
        Category = "Overweight"

    else :
        Category = "Obese"
    return Category

Category = BMI_cat(BMI)

### Closing message
print(name + ", your BMI is: " + str(BMI) + ". Your weight category therefore is: " + Category)