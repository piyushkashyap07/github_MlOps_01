def addition(x, y):
    """
    Adds two numbers.

    Parameters:
    - x: The first number.
    - y: The second number.

    Returns:
    The sum of x and y.
    """
    return x + y

def subtraction(x, y):
    """
    Subtracts one number from another.

    Parameters:
    - x: The number to be subtracted from.
    - y: The number to subtract.

    Returns:
    The result of subtracting y from x.
    """
    return x - y

def main():
    # Example usage
    num1 = 10
    num2 = 5

    added_value = addition(num1, num2)
    subtracted_value = subtraction(num1, num2)

    # Print results
    print(f"Addition: {num1} + {num2} = {added_value}")
    print(f"Subtraction: {num1} - {num2} = {subtracted_value}")

if __name__ == "__main__":
    main()