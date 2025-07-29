print("📅 Welcome to the simple calculator!\n")

print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter your choice number: ")

if choice not in ['1', '2', '3', '4']:
    print("\n❌ Error: Invalid choice! Please select 1, 2, 3, or 4.")
else:
    try:
        number_one = float(input("Enter your first number: "))
        number_two = float(input("Enter your second number: "))

        if choice == '1':
            result = number_one + number_two
            print(f"\n🧮 The sum: {number_one} + {number_two} = {result}")

        elif choice == '2':
            result = number_one - number_two
            print(f"\n🧮 The subtraction: {number_one} - {number_two} = {result}")

        elif choice == '3':
            result = number_one * number_two
            print(f"\n🧮 The multiplication: {number_one} × {number_two} = {result}")

        elif choice == '4':
            if number_two != 0:
                result = number_one / number_two
                print(f"\n🧮 The division: {number_one} ÷ {number_two} = {result}")
            else:
                print("\n❌ Error: Cannot divide by zero.")

    except ValueError:
        print("\n❌ Error: Please enter valid numbers only.")
