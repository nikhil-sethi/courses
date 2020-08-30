# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

def sortcrit(list):
    return list.end

def compute_optimal_points(segments, output):
    n1 = len(segments)
    if n1 == 0:
        return output
    else:
        temp = segments[:]
        for j in range(1, n1):
            if segments[-j].start <= segments[0].end: # check from right
                del(temp[-j + n1]) # delete from left
        segments = temp[:]
        output.append(segments[0].end)
        del(segments[0])
        return compute_optimal_points(segments, output)

if __name__ == '__main__':
n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    input_segments.sort(key=sortcrit)
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments, [])
    print(len(output_points))
    print(*output_points)

