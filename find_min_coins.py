from constants import COINS


def find_min_coins(sum):
    min_coins = [float('inf')] * (sum + 1)
    min_coins[0] = 0
    last_coin_used = [0] * (sum + 1)

    for s in range(1, sum + 1):
        for coin in COINS:
            if s >= coin:
                if min_coins[s - coin] + 1 < min_coins[s]:
                    min_coins[s] = min_coins[s - coin] + 1
                    last_coin_used[s] = coin
    
    result = {}
    current_sum = sum

    while current_sum > 0:
        coin = last_coin_used[current_sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1

        current_sum -= coin
    return result


# sum = 113
# res = find_min_coins(sum)

# print(f"Сума: {sum}")
# print(f"Результат DP: {res}")