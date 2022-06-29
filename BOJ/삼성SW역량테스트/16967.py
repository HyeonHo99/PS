import sys

if __name__ == "__main__":
    H, W, X, Y = map(int, sys.stdin.readline().rstrip().split())
    A_map = [[-1 for _ in range(W)] for _ in range(H)]
    B_map = []
    for i in range(H+X):
        B_map.append(list(map(int, sys.stdin.readline().rstrip().split())))

    ## only A
    for r in range(H):
        for c in range(W):
            if (r < X) or (c < Y):
                A_map[r][c] = B_map[r][c]
    ## both A and B
    for r in range(H):
        for c in range(W):
            if (r >= X) and (c >= Y):
                A_map[r][c] = B_map[r][c] - A_map[r-X][c-Y]


    for A_row in A_map:
        for row_el in A_row:
            print(row_el,end=" ")
        print()