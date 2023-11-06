def calculate_fibonacci_series(n):
    a, b = 0, 1
    step_count = 0
    fibonacci_series = []

    for i in range(n):
        step_count += 1
        fibonacci_series.append(a)
        temp = a  # Store the current value of 'a' in a temporary variable
        a = b     # Update 'a' with the current value of 'b'
        b = temp + b

    return fibonacci_series, step_count

def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    

# Input from the user
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Calculate the Fibonacci series and step count
fibonacci_series, step_count = calculate_fibonacci_series(n)

print(f"Fibonacci Series for the first {n} terms: {fibonacci_series}")
print(f"Step count: {step_count}")
for i in range(n):
        print(recursive_fibonacci(i))
#print("Step count: " + str(step_count))