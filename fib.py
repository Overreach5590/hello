def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize Fibonacci sequence with first two terms

    # Generate Fibonacci sequence up to the nth term
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

# Example usage:
num_terms = 10
print(fibonacci(num_terms))
