
def calculate_gross_salary(basic_salary, allowance):
    """Return gross salary = basic salary + allowance."""
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    """Return the tax amount, where tax_rate is a percentage (e.g. 10 for 10%)."""
    return gross_salary * tax_rate / 100


def calculate_net_salary(gross_salary, tax):
    """Return net (take-home) salary = gross salary - tax."""
    return gross_salary - tax



def read_text(prompt):
    """Ask for text and keep asking until it is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def read_non_negative_number(prompt):
    """Ask for a number and keep asking until it is a valid number >= 0."""
    while True:
        raw_value = input(prompt)
        try:
            number = float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if number >= 0:
            return number
        print("The value cannot be negative.")


def read_tax_rate(prompt):
    """Ask for a tax rate percentage and keep asking until it is between 0 and 100."""
    while True:
        rate = read_non_negative_number(prompt)
        if rate <= 100:
            return rate
        print("Tax rate cannot be more than 100%.")



def format_salary_slip(name, basic_salary, allowance, gross_salary,
                       tax_rate, tax, net_salary):
    """Return the salary slip as a printable multi-line string."""
    lines = [
        "=" * 40,
        "          EMPLOYEE SALARY SLIP",
        "=" * 40,
        f"Employee Name : {name}",
        f"Basic Salary  : {basic_salary:,.2f}",
        f"Allowance     : {allowance:,.2f}",
        "-" * 40,
        f"Gross Salary  : {gross_salary:,.2f}",
        f"{f'Tax ({tax_rate:g}%)':<14}: {tax:,.2f}",
        "-" * 40,
        f"Net Salary    : {net_salary:,.2f}",
        "=" * 40,
    ]
    return "\n".join(lines)


def display_salary_slip(slip_text):
    """Print the formatted salary slip."""
    print()
    print(slip_text)



def main():
    """Collect input, run the calculations in order, and show the result."""
    name = read_text("Enter employee name: ")
    basic_salary = read_non_negative_number("Enter basic salary: ")
    allowance = read_non_negative_number("Enter allowance: ")
    tax_rate = read_tax_rate("Enter tax rate (%): ")

    gross_salary = calculate_gross_salary(basic_salary, allowance)
    tax = calculate_tax(gross_salary, tax_rate)
    net_salary = calculate_net_salary(gross_salary, tax)

    slip = format_salary_slip(name, basic_salary, allowance, gross_salary,
                              tax_rate, tax, net_salary)
    display_salary_slip(slip)


if __name__ == "__main__":
    main()
