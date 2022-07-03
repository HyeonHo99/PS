import sys

d_r = [1,0,-1,0]
d_c = [0,1,0,-1]

def calculate_satisfaction(classroom,like_dict,N):
    ret = 0
    for r in range(N):
        for c in range(N):
            num_likes = 0
            for i in range(4):
                n_r = r + d_r[i]
                n_c = c + d_c[i]
                ## idx error caution
                if (0<= n_r <= N-1 and 0 <= n_c <= N-1) and (classroom[n_r][n_c] in like_dict[classroom[r][c]]):
                    num_likes += 1
            ret = ret + 10**(num_likes-1) if num_likes > 0 else ret
    return ret

def find_and_update(classroom,liked_ones,cur,N,occupied):
    like_level_dict = dict()
    for i in range(5):
        like_level_dict[i] = []

    for r in range(N):
        for c in range(N):
            if not occupied[r][c]:
                like_score = 0
                num_sparse = 0
                for i in range(4):
                    n_r = r + d_r[i]
                    n_c = c + d_c[i]
                    if (0 <= n_r <= N-1) and (0 <= n_c <= N-1):
                        if classroom[n_r][n_c] in liked_ones:
                            like_score += 1
                        if classroom[n_r][n_c] == 0:
                            num_sparse += 1
                like_level_dict[like_score].append((r,c,num_sparse))

    for i in range(4,-1,-1):
        num_candidates = len(like_level_dict[i])
        if num_candidates == 0:
            continue
        elif num_candidates == 1:
            r,c,_ = like_level_dict[i][0]
            classroom[r][c] = cur
            occupied[r][c] = True
            break
        else:
            # candidates = sorted(like_level_dict[i],lambda x:(-x[2],x[0],x[1]))
            candidates = sorted(like_level_dict[i],key = lambda x:-x[2])
            r,c,_ = candidates[0]
            classroom[r][c] = cur
            occupied[r][c] = True
            break



if __name__ == "__main__":
    N = int(input())
    classroom = [[0]*N for _ in range(N)]
    like_dict = dict()
    order_list = []
    occupied = [[False]*N for _ in range(N)]
    for _ in range(N*N):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        order_list.append(row[0])
        like_dict[row[0]] = row[1:]

    for i, cur in enumerate(order_list):
        if i == 0:
            classroom[1][1] = cur
            occupied[1][1] = True
        else:
            find_and_update(classroom,like_dict[cur],cur,N,occupied)
        # for a in classroom:
        #     print(a)
        # print("="*10)

    total_satisfaction = calculate_satisfaction(classroom,like_dict,N)
    print(total_satisfaction)