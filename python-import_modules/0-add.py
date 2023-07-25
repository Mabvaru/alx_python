def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b

# If the module is not being imported, execute the following code
if __name__ == "__main__":
    # Assign values to variables a and b
    a = 1
    b = 2

    # Calculate the result using the add function
    result = add(a, b)

    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, result))
