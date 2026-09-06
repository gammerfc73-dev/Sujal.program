print("🧮 PYTHON CALCULATOR")
print("--------------------")

while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("❌ Cannot divide by zero!")
                continue
            result = num1 / num2
        else:
            print("❌ Invalid operator!")
            continue

        print("✅ Result:", result)

        again = input("Calculate again? (y/n): ")

        if again.lower() != "y":
            print("Goodbye! 👋")
            break

    except ValueError:
        print("❌ Please enter valid numbers.")
