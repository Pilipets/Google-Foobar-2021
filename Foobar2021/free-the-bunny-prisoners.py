from itertools import combinations
def solution(n, m):
    # Stores stock of each bunny - indices of keys each bunny holds
    bunny_stock = [[] for _ in range(n)]

    m = n - m + 1
    # m bunnies hold the same key - we need to figure out which ones.
    # One way of distribution the keys is generating the combinations of bunnies,
    # where one represents a valid cell opening tuple.
    # 
    # To each combination we assign the number from a zero-based increasing range and
    # add that number to each of the selected bunnies.

    # In the end, for each bunny we have indices of tuples it comprises to.
    for cell, bunny_arr in enumerate(combinations(range(n), m)):
        print(cell, bunny_arr)
        for bunny_idx in bunny_arr:
            bunny_stock[bunny_idx].append(cell)

    return bunny_stock