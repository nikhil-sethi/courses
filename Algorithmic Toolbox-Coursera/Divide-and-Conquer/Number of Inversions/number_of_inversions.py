# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def combine(a,b, ca, cb):
    A = []
    c = 0
    while a != [] and b != []:
        if a[0] > b[0]:
            A.append(b[0])
            c += len(a)
            del b[0]
        else:
            A.append(a[0])
            del a[0]

    if a==[] and b!=[]:
        for i in range(len(b)):
            A.append(b[i])
    elif b==[] and a!=[]:
        for i in range(len(a)):
            A.append(a[i])
    print(A, c+ca+cb)
    return A, c+ca+cb


def compute_inversions(A):

    l=len(A)
    if l == 1:
        return A, 0
    a, ca = compute_inversions(A[:l//2])
    b, cb = compute_inversions(A[l//2:])
    return combine(a,b, ca, cb)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    array, inversions = compute_inversions(elements)
    print(inversions)
