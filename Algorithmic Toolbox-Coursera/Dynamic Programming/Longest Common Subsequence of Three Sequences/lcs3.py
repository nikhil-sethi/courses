# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    n=len(first_sequence)
    m = len(second_sequence)
    q = len(third_sequence)

    d = np.zeros((n+1, m+1, q+1))
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, q+1):
                mismatch = d[i-1, j-1, k-1]
                match = mismatch+1
                in1 = d[i-1, j-1, k]
                del1 = d[i-1, j, k-1]
                del2 = d[i - 1, j, k]
                in2 = d[i, j - 1, k-1]
                in3 = d[i, j - 1, k]
                del3 = d[i, j, k - 1]
                if first_sequence[i-1]==second_sequence[j-1]==third_sequence[k-1]:
                    d[i, j, k]=match
                else:
                    d[i, j, k]=max(mismatch, in1, del1, in2, del2, del3, in3)
    return d

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
