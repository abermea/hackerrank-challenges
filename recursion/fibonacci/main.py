def fibonacci(n):
    return fib(0, 1, n)

def fib(p, pp, n):
    if n == 0:
        return p
    else:
        return fib(pp, p + pp, n - 1)