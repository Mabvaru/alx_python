def fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)

    return sequence[:n]
