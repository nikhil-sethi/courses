# python3
import numpy as np
from random import randint

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def partition3(array, left, right):
    j = left
    k = left
    for i in range(left+1, right+1):
        if array[i] == array[left]:
            k = k + 1
            array[k], array[i] = swap(array[k], array[i])
        if array[i] < array[left]:
            k = k+1
            array[k], array[i] = swap(array[k], array[i])
            j = j + 1
            array[j], array[k] = swap(array[j], array[k])
    array[left], array[j] = swap(array[left], array[j])
    return j, k

def partition(array, left, right):
    j = left
    for i in range(left+1, right+1):
        if array[i] < array[left]:
            j = j+1
            array[j], array[i] = swap(array[j], array[i])
    array[left], array[j] = swap(array[left], array[j])
    return j, j

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m, n = partition3(array, left, right)
    randomized_quick_sort(array, n+1, right)
    randomized_quick_sort(array, left, m-1)
#     make a call to partition3 and then two recursive calls
# to randomized_quick_sort
# s

if __name__ == '__main__':
    # input_n = int(input())
    # elements = list(map(int, input().split()))
    # assert len(elements) == input_n
    elements = np.random.randint(10, size=np.random.randint(10000))
    print(len(elements))
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print('result=', *elements)
