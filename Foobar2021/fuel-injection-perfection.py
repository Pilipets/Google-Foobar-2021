def solution(n):
    n, steps = int(n), 0
    while n > 1:
        if n & 1:
            if n & 2 and n != 3: n += 1
            else: n -= 1
        else:
            n >>= 1
        steps += 1
    return steps

print(solution('15'))