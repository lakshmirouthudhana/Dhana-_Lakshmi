def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Do enter only +ve values greater than 0")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi():
    name = input("Enter your name: ")
    
    # 1. Height Unit Selection & Validation
    print("\nChoose your height unit:")
    print("1. Centimeters (cm)")
    print("2. Feet (ft)")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        height_cm = get_positive_float("Enter height in cm: ")
        height_m = height_cm / 100
    elif choice == '2':
        height_ft = get_positive_float("Enter height in feet: ")
        height_m = height_ft * 0.3048
    else:
        print("Invalid choice. Defaulting to meters directly.")
        height_m = get_positive_float("Enter height in meters: ")
        
    # 2. Weight input for BMI calculation
    weight_kg = get_positive_float("Enter weight in kg: ")
    
    # 3. Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)
    
    # 4. Classification & Output
    print(f"\n--- Results for {name} ---")
    if bmi < 18.5:
        print(f"{name} is Underweight and bmi is {bmi}")
    elif bmi <= 24.9:
        print(f"{name} is Healthy and bmi is {bmi}")
    elif bmi <= 30:
        print(f"{name} is Overweight and bmi is {bmi}")
    else:
        print(f"{name} is in Obese Category and bmi is {bmi}")

# Run the program
if __name__ == "__main__":
    calculate_bmi()
