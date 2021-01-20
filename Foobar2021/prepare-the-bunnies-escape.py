from collections import deque

def solution(grid):
    k = 1
    n, m = len(grid), len(grid[0])
    if k >= n+m-3:
        return n+m-2
        
    q = deque([(0,0,k)])
    used = [[-1 for _ in range(m)] for _ in range(n)]

    step, sdist = 1, n + m - 2
    while q:
        dsdist = sdist
        for _ in range(len(q)):
            i, j, b = q.popleft()
            if used[i][j] > b: continue

            for i, j in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if not (n > i >= 0 <= j < m): continue
                        
                nb = b - grid[i][j]
                if used[i][j] >= nb: continue
    
                dist = n + m - i - j - 2
                if (dist-1 <= nb and dist == sdist-1): return step + dist + 1
                    
                dsdist = min(dist, dsdist)
                q.append((i, j, nb))
                used[i][j] = nb

        sdist, step = dsdist, step + 1
    return -1

print(solution([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]))