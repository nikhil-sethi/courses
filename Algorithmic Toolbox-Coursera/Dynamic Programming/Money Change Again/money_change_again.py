# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    Change = [0, 1, 2, 1, 1]
    for i in range(5, money+1):
        Change.append(min(Change[i-3]+1, Change[i-4]+1, Change[i-1]+1))
    return Change[money]

if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
