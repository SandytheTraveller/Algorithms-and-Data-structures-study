def fibonacci(n):
    # base case
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # recursive calls

nterms = 10
fibo_seq = [fibonacci(n) for n in range(nterms)]

print("Fibonacci sequence: ", fibo_seq)