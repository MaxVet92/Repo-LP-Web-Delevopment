### Ask for height and weight
def get_info():
    ## enter name
    while True:
        name = input("Enter your name:")
        if name != "" and name.isalpha():
            break
        print("Input not valid. Please try again")

    ## enter weight
    while True:
        try:
            weight = int(input("Hello, " + name + ". Please enter your weight in Kg"))
            if weight <= 0:
                print("Your weigt must be greater than 0")
                continue
            break
        except ValueError:
            print("Please type a valid number")
        

    ## enter height
    while True:
        try:
            height = int(input("Great, now please enter your height in cm")) / 100
            if height <= 0:
                print("Invalid height. Please try again.")
                continue
            break
        except:
            ValueError
            print("You didn't type in a number please try again")
    return name, weight, height

### save the data
name, weight, height = get_info()

### calculate the BMI
def BMI(name, weight, height):
    BMI = weight / height**2
    print(name + ", your BMI is: " + str(BMI))
    return BMI

### Calculate BMI category

def BMI_cat(name,weight,height):
    if round(BMI(name, weight, height), 2) < 18.5:
        Category = "Underweight"

    elif round(BMI(name, weight, height), 2) <= 24.9:
        Category = "Normal weight"

    elif round(BMI(name, weight, height), 2) <= 29.9:
        Category = "Overweight"

    else :
        Category = "Obese"
    return Category

Category = BMI_cat(name,weight,height)
print(name + ", your BMI is: " + str(round(BMI(name, weight, height), 2)) + ". Your weight category therefore is: " + Category)