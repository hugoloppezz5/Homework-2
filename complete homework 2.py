print("I am going to help you calculate your net salary.")

# Get user input
name = input("How should I call you? ")

try:
    # Get and validate gross salary
    gross_salary = float(input("What is your gross salary? "))
    gross_salary = int(gross_salary)  # Convert to integer for consistency

    # Get number of children
    children = int(input("How many children do you have? "))

    # Determine income tax rate
    income_tax = 10 if gross_salary < 1000 else \
                 12 if gross_salary < 2000 else \
                 14 if gross_salary < 4000 else 18

    # Calculate tax reduction based on children
    tax_cut = children * (1 if gross_salary < 2000 else 0.5)

    # Calculate total tax rate after reductions
    total_tax_rate = max(0, income_tax - tax_cut)  # Ensure tax rate is not negative

    # Compute net salary
    net_salary = gross_salary * (1 - total_tax_rate / 100)

    # Display result
    print(f"{name}, your net salary is {net_salary:.2f}")

except ValueError:
    print("Please enter valid numerical values!")
