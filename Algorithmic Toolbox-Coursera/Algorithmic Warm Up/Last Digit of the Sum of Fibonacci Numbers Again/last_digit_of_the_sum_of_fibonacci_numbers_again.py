# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10

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

def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    F = [fib(from_index), fib(from_index+1)]
    s = sum(F) % 10
    for i in range(from_index+2, to_index+1):
        F = [F[-1], (F[-1] + F[-2]) % 10]  # [1,1], [1,2], [2,3]
        # print(F)
        s += F[-1]
        s = s % 10
    return s


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
