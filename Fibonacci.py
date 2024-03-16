# Function to generate Fibonacci sequence up to n
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Get user input for n
n = int(input("Enter the value of n: "))

# Generate and print Fibonacci sequence up to n
print(fibonacci(n))