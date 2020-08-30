# python3
import numpy as np

def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    a=len(first_sequence)
    b=len(second_sequence)
    count = 0
    d=np.zeros((a+1, b+1), dtype=int)

    for i in range(1, a+1):
        for j in range(1, b+1):
            mismatch = d[i-1, j-1]
            match = mismatch+1
            insertion = d[i-1, j]
            deletion = d[i, j-1]
            if first_sequence[i-1] == second_sequence[j-1]:
                d[i, j] = match#max(match, insertion, deletion)
                count += 1
            else:
                d[i,j] = max(mismatch, insertion, deletion)
    return d[-1, -1]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
