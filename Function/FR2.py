def factorial(n):
    if( n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
value=factorial(5)
print(f"Factorial becomes: {value}")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
