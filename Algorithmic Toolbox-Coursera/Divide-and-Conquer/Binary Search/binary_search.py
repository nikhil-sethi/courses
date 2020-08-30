# python3
import numpy as np

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, low, high, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    if high < low:
        return -1
    mid = low + (high-low)//2
    if keys[mid] == query:  #11==12
        return mid
    elif query < keys[mid]:  #
        high = mid-1
    elif keys[mid] < query: # 11<12
        low = mid+1

    return binary_search(keys, low, high, query)

def binary_searchwrapper(keys, query):
    return binary_search(keys, 0, len(keys)-1, query)

# def stress_test(m, p):
#     while True:
#         tkeys = np.sort(np.unique(np.random.randint(0, p, size=np.random.randint(3, m))))
#         tquery = np.random.randint(p)
#         print(tkeys, tquery)
#         out1 = linear_search(tkeys, tquery)
#         out2 = binary_searchwrapper(tkeys, tquery)
#
#         if out1 == out2:
#             print('ok')
#         else:
#             print('wrong answer'
#             print(out1,'\n', out2)
#             break

if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_searchwrapper(input_keys, q), end=' ')
