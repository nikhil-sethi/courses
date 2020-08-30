# python3


def money_change(money, count=0):
    assert 0 <= money <= 10 ** 3
    count = money//10
    money = money % 10
    count += money//5
    count += money % 5
    return count


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
