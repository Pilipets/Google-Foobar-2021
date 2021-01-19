def get_p(val, e):
    if e == val: return -1

    st = 1
    while True:
        e -= 1
        m = st + (e-st)//2

        if m == val or e == val: return e+1
        elif val < m: e = m
        else: st = m

def solution(h, q):
    e = (1 << h) - 1
    return [get_p(x, e) for x in q]

print(solution(5, [18]))