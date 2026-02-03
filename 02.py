import datetime

def main():
    # 1. Get two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # 2. Perform calculations
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    # Handle division by zero
    div = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

    # 3. Format the output string
    # Using f-strings to limit decimals to 2 places as requested
    timestamp = datetime.datetime.now().strftime("%b %d, %Y - %I:%M %p")
    
    results = (
        f"[{timestamp}]\n"
        f"{num1} + {num2} = {add:.2f}\n"
        f"{num1} - {num2} = {sub:.2f}\n"
        f"{num1} * {num2} = {mul:.2f}\n"
        f"{num1} / {num2} = {div if isinstance(div, str) else f'{div:.2f}'}\n"
        f"{'-'*20}\n"
    )

    # 4. Display results to the user
    print("\nCalculations:")
    print(results)

    # 5. Save/Append to calculator_history.txt
    # 'a' mode opens the file for appending instead of 'w' (writing/overwriting)
    with open("calculator_history.txt", "a") as file:
        file.write(results)
    
    print("History updated in calculator_history.txt")

if __name__ == "__main__":
    main()