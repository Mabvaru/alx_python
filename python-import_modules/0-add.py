if __name__ == "__main__":
    # Import the add function from add_0.py
    from add_0 import add

    # Define variables a and b
    a = 1
    b = 2

    # Calculate the result using the add function
    result = add(a, b)

    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, result))
