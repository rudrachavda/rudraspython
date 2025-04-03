def generate_fibonacci(n):
    fibonacci_sequence = [0,1]
    while len (fibonacci_sequence) < n:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    return fibonacci_sequence

n = int(input("How many terms do you want?"))
fib_sequence = generate_fibonacci(n)
print (fib_sequence)

