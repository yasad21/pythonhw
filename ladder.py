def my_steps(n):
    if (n<1 or n> 25):
        raise ValueError("Input must be between 1 and 25")

    if n <= 2:
        return n
    else:
        a, b = 1, 2
        for I in range(3, n + 1):
            a, b = b, a + b
        return b


