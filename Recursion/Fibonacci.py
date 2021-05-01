def Fibonacci(n):
    assert 0 <= n == int(n), 'The number must be >=0 i.e. positive integer'

    if n in [0, 1]:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(4))
