def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return a - b

if __name__ == "__main__":
    # Define variables a and b
    a = 1
    b = 2

    # Calculate the result using the add function
    result = add(a, b)

    # Print the output for the test case
    print("a = {} and b = {} FAKE add() => a - b".format(a, b, result))

    # Define variables a and b
    a = 10
    b = 30

    # Calculate the result using the add function
    result = add(a, b)

    # Print the output for the test case
    print("a = {} and b = {} FAKE add() => a - b".format(a, b, result))

    # Define variables a and b
    a = -10
    b = 30

    # Calculate the result using the add function
    result = add(a, b)

    # Print the output for the test case
    print("a = {} and b = {} FAKE add() => a - b".format(a, b, result))

    # Define variables a and b
    a = -10
    b = -30

    # Calculate the result using the add function
    result = add(a, b)

    # Print the output for the test case
    print("a = {} and b = {} FAKE add() => a - b".format(a, b, result))

    # Define variables a and b
    a = 5
    b = "H"

    # Calculate the result using the add function
    result = add(a, b)

    # Print the output for the test case
    print("a = {} and b = {} FAKE add() => a - b".format(a, b, result))
