def length(x: float):
    print("Menu:\n")
    print("\t1.Meters to Kilometers\n")
    print("\t2.Feet to Meters\n")
    print("\t3.Inches to Centimeters\n")
    print("\t4.Miles to Kilometers\n")
    
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            result = x / 1000
            return f"{x}m => {result}km"
        case 2:
            result = x * 0.3048
            return f"{x}feet => {result}m"
        case 3:
            result = x * 2.54
            return f"{x}inches => {result}cm"
        case 4:
            result = x * 1.60934
            return f"{x}miles => {result}km"
        case _:
            return "We are still working on other units :)"

def mass(x: float):
    print("Menu:\n")
    print("\t1.Kilograms to Grams\n")
    print("\t2.Pounds to Kilograms\n")
    print("\t3.Ounces to Grams\n")
    
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            result = x * 1000
            return f"{x}kg => {result}g"
        case 2:
            result = x * 0.453592
            return f"{x}pounds => {result}kg"
        case 3:
            result = x * 28.3495
            return f"{x}ounces => {result}g"
        case _:
            return "We are still working on other units :)"

def temp(x: float):
    print("Menu:\n")
    print("\t1.Celsius to Fahrenheit\n")
    print("\t2.Fahrenheit to Celsius\n")
    print("\t3.Celsius to Kelvin\n")
    
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            result = (x * 9/5) + 32
            return f"{x}°C => {result}°F"
        case 2:
            result = (x - 32) * 5/9
            return f"{x}°F => {result}°C"
        case 3:
            result = x + 273.15
            return f"{x}°C => {result}K"
        case _:
            return "We are still working on other units :)"

def time(x: float):
    print("Menu:\n")
    print("\t1.Minutes to Seconds\n")
    print("\t2.Hours to Minutes\n")
    print("\t3.Days to Hours\n")
    
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            result = x * 60
            return f"{x} minutes => {result} seconds"
        case 2:
            result = x * 60
            return f"{x} hours => {result} minutes"
        case 3:
            result = x * 24
            return f"{x} days => {result} hours"
        case _:
            return "We are still working on other units :)"

def volume(x: float):
    print("Menu:\n")
    print("\t1.Liters to Milliliters\n")
    print("\t2.Gallons (US) to Liters\n")
    print("\t3.Cups (US) to Milliliters\n")
    
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            result = x * 1000
            return f"{x} liters => {result} ml"
        case 2:
            result = x * 3.78541
            return f"{x} gallons => {result} liters"
        case 3:
            result = x * 236.588
            return f"{x} cups => {result} ml"
        case _:
            return "We are still working on other units :)"

def speed(x: float):
    print("Menu:\n")
    print("\t1.Kilometers per Hour to Miles per Hour\n")
    print("\t2.Meters per Second to Kilometers per Hour\n")
    
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            result = x * 0.621371
            return f"{x} kph => {result} mph"
        case 2:
            result = x * 3.6
            return f"{x} m/s => {result} kph"
        case _:
            return "We are still working on other units :)"

def energy(x: float):
    print("Menu:\n")
    print("\t1.Joules to Calories\n")
    
    choice = int(input("Choose an option: "))
    match choice:
        case 1:
            result = x / 4.184
            return f"{x} joules => {result} calories"
        case _:
            return "We are still working on other units :)"

# Main program
ok = True
while ok:
    print("\t-----Welcome to MetricMate: Unit Converter-----\t")
    print("\nMenu:\n")
    print("\t1.Length\n")
    print("\t2.Mass\n")
    print("\t3.Temperature\n")
    print("\t4.Time\n")
    print("\t5.Volume\n")
    print("\t6.Speed\n")
    print("\t7.Energy\n")
    print("\t8.Team Notes\n")

    print("Choose a number from the menu above:")
    choice = int(input("\n"))

    match choice:
        case 1:
            value = float(input("Enter value: "))
            print("Result: " + length(value))
        case 2:
            value = float(input("Enter value: "))
            print("Result: " + mass(value))
        case 3:
            value = float(input("Enter value: "))
            print("Result: " + temp(value))
        case 4:
            value = float(input("Enter value: "))
            print("Result: " + time(value))
        case 5:
            value = float(input("Enter value: "))
            print("Result: " + volume(value))
        case 6:
            value = float(input("Enter value: "))
            print("Result: " + speed(value))
        case 7:
            value = float(input("Enter value: "))
            print("Result: " + energy(value))
        case 8:
            print("Team Notes: Stay tuned for the upcoming updates!")
        case _:
            print("Invalid option, please try again!")

    print("\nDo you want to convert another time? (yes/no)")
    ok = input().lower() == "yes"
    if not ok:
        print("Goodbye MetricMate!")
