def solution(st, len):
    def xor_from_1(r):
        return [r, 1, r+1, 0][r % 4]

    res = 0
    for r_shift in range(len-1, -1, -1):
        res ^= (xor_from_1(st-1) ^ xor_from_1(st+r_shift))
        st += len
    return res

print(solution(0,3))