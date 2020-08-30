# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    # find nth fibonacci number
    F = [0, 1]
    if n == 0:
        return F[0]
    if n == 1:
        return F[1]
    for i in range(2, n + 1):
        F.append(F[i - 2] + F[i - 1])
    return F[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
