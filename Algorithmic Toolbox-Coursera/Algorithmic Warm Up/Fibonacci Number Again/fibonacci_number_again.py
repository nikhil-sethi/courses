# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def pisano(m):
    F = [0, 1]
    if m <= 1:
        return m
    p = 2
    while True:
        F = [F[-1], F[-1] + F[-2]]  #[1,1], [1,2], [2,3]
        p += 1  #3, 4, 5
        if F[-1] % m == 1 and F[-2] % m == 0: #[1,1], [1,0], [0,1]
            break
    return p-2

def fib(n):
    # find nth fibonacci number
    F = [0, 1]
    if n == 0:
        return F[0]
    if n == 1:
        return F[1]
    for i in range(2, n + 1):
        F.append(F[i - 2] + F[i - 1])
    return F[-1]

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    p = pisano(m)
    if n < p:
        print(fib(n) % m)
    else:
        n = n % p
        return fibonacci_number_again(n, m)

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
