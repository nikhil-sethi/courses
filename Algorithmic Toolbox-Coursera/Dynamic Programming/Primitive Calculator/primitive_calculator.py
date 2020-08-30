# python3


def compute_operations_greedy(n):
    assert 1 <= n <= 10 ** 6
    nums = []
    if n == 1:
        return
    if n % 3 == 0:
        nums.append(n//3)
    if n % 2 == 0:
        nums.append(n//2)
    else:
        nums.append(n - 1)

    print(min(nums))
    return compute_operations(min(nums))

def compute_operations(n):
    nums=[0,0,1,1]
    for i in range(4, n+1):
        if i%3==0:
            nums.append(min(nums[i // 3]+1, nums[i-1]+1))
        elif i%2==0:
            nums.append(min(nums[i // 2] + 1, nums[i - 1] + 1))
        else:
            nums.append(nums[i-1]+1)
    return nums[-1]

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
