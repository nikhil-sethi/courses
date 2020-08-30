# Uses python3
# least common multiple
import random

inp = input()
inp = [int(num) for num in inp.split()]

def GCF(inp):
    if min(inp) == 0:
        return max(inp)
    a = max(inp) % min(inp)
    b = min(inp)
    return GCF([a, b])


# NAIVE
def lcm_naive(inp):

    for num in range(max(inp), inp[1] * inp[0] + 1):
        if num % inp[1] == 0 and num % inp[0] == 0:
            return num


def lcm_fast(inp):

    gcf = GCF(inp)  # compute GCF
    out = inp[1] * inp[0] // gcf
    return out  # multiply both numbers and divide by GCF

print(lcm_fast(inp))

# stress test
#m = 8000 # max input size

#while True:
#   inp = [random.randint(1, m), random.randint(1, m)]
#    print(inp)
#    res2 = lcm_fast(inp)
#    res1 = lcm_naive(inp)
#    if res1 == res2:
#        print('OK')
#    else:
#        print('Wrong Answer', res1, res2)
#        break

