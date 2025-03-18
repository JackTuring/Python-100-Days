def fibonacci_recursive(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1;
    for _ in range(n+1):
        a, b = b, a + b
        print(a)

n = int(input("please enter a number: "))
fibonacci_iterative(n)