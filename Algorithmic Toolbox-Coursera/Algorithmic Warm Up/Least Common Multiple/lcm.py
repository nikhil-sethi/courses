# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple

def GCF(inp):
    if min(inp) == 0:
        return max(inp)
    a = max(inp) % min(inp)
    b = min(inp)
    return GCF([a, b])

def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    inp = [a, b]
    gcf = GCF(inp)  # compute GCF
    out = inp[1] * inp[0] // gcf
    return out  # multiply both numbers and divide by GCF


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
