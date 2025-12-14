from constants import COINS


def find_coins_greedy(sum):
    change = {}

    for coin in COINS:
        count = sum // coin

        if count > 0:
            change[coin] = count
            sum = sum % coin

    return change


# sum = 113
# result = find_coins_greedy(sum)
# print(f"Сума: {sum}")
# print(f"Результат: {result}")