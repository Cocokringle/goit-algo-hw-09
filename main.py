import time

from find_coins_greedy import  find_coins_greedy
from find_min_coins import  find_min_coins


def compare_algorithms(sum):
    print(f"--- Порівняння для суми: {sum} ---")

    start_time = time.time()
    find_coins_greedy(sum)
    end_time = time.time()
    greedy_time = end_time - start_time
    print(f"Жадібний алгоритм: {greedy_time:.6f} сек")

    start_time = time.time()
    find_min_coins(sum)
    end_time = time.time()
    dp_time = end_time - start_time
    print(f"Динамічне програмування: {dp_time:.6f} сек")
    
    if dp_time > 0:
        print(f"Жадібний швидше в {dp_time / greedy_time:.1f} разів")


compare_algorithms(10000)