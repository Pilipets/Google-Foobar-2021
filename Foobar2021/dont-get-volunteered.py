def solution(src, dest):
    visited = [[False for _ in range(8)] for _ in range(8)]
    dx = [-2, -2, -1, -1,  1, 1,  2, 2]
    dy = [-1,  1, -2,  2, -2, 2, -1, 1]

    if src == dest: return 0

    src, dest = (src // 8, src % 8), (dest // 8, dest % 8)
    level = [src]
    visited[src[0]][src[1]] = True

    step = 1
    while level:
        next = []
        for i, j in level:
            for idx in range(8):
                n_i, n_j = i + dx[idx], j + dy[idx]
                if (n_i, n_j) == dest: return step
                if (n_i >= 0 and n_i < 8 and n_j >= 0 and n_j < 8 and not visited[n_i][n_j]):
                    visited[n_i][n_j] = True
                    next.append((n_i, n_j))
        level = next
        step += 1
    return -1

print(solution(19, 36))