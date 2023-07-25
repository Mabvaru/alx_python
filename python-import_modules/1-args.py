import sys

if __name__ == "__main__":
    # Get the command-line arguments (excluding the script name itself)
    args = sys.argv[1:]

    # Get the number of arguments
    num_args = len(args)

    # Print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Print the list of arguments, one per line
    for idx, arg in enumerate(args, start=1):
        print(f"{idx}: {arg}")
