# python3
import numpy as np

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    l = len(elements)
    # print(elements)
    if l == 1:
        return elements[0]
    a = majority_element(elements[:l // 2])
    b = majority_element(elements[l // 2:])

    if a != -1:  # if majority in 1st half
        count = 0
        for i in range(l):  # count occurences of majority element in overall array
            if elements[i] == a:
                count = count + 1
        if count > l // 2:  # if more than half then declare same mahority for whole
            return a
    if b != -1:  # if 1st half doesnt have major element check with 2nd
        count = 0
        for i in range(l):
            if elements[i] == b:
                count = count + 1
        if count > l // 2:
            return b

    return -1  # if no majority return 0 in any case


def majority_elementwrap(elements):
    if majority_element(elements) != -1:
        return 1
    return 0

def stress_test(n):
    while True:
        m = np.random.randint(2,n)
        print('m=',m)
        elem = np.random.randint(m//6+1, size=m)
        out1 = majority_element_naive(list(elem))
        print(out1)
        out2 = majority_elementwrap(elem)
        print(out2)
        print('elem=', elem)
        if out1 == out2:
            print('ok')
        else:
            print('wrong answer')
            print('out1=', out1, 'out2=', out2)
            break
if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
    # print(majority_elementwrap([1, 2, 2, 4, 5]))
    # stress_test(100000)