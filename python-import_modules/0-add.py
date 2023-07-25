def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return a - b

# Define variables a and b
a = 1
b = 2

# Calculate the result using the add function
result = add(a, b)

# Define output string for the test case
output = "a = {} and b = {} FAKE add() => a - b".format(a, b, result)

# Define variables a and b
a = 10
b = 30

# Calculate the result using the add function
result = add(a, b)

# Update the output string for the new test case
output += "\n" + "a = {} and b = {} FAKE add() => a - b".format(a, b, result)

# Define variables a and b
a = -10
b = 30

# Calculate the result using the add function
result = add(a, b)

# Update the output string for the new test case
output += "\n" + "a = {} and b = {} FAKE add() => a - b".format(a, b, result)

# Define variables a and b
a = -10
b = -30

# Calculate the result using the add function
result = add(a, b)

# Update the output string for the new test case
output += "\n" + "a = {} and b = {} FAKE add() => a - b".format(a, b, result)

# Define variables a and b
a = 5
b = "H"

# Calculate the result using the add function
result = add(a, b)

# Update the output string for the new test case
output += "\n" + "a = {} and b = {} FAKE add() => a - b".format(a, b, result)

# Print the output for all the test cases together
print(output)
