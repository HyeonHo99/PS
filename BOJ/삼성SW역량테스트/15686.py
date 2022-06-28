import sys
from itertools import combinations

def get_house_chicken_distance(house, chicken_list):
    loc = [-1,-1]
    dist = 98
    for chicken in chicken_list:
        if abs(chicken[0]-house[0]) + abs(chicken[1]-house[1]) < dist:
            loc[0] = chicken[0]
            loc[1] = chicken[1]
            dist = abs(chicken[0]-house[0]) + abs(chicken[1]-house[1])
    return loc,dist

def get_city_chicken_distance(house_list, chicken_list):
    dist = 0
    for house in house_list:
        _, chicken_dist = get_house_chicken_distance(house,chicken_list)
        dist += chicken_dist
    return dist

if __name__ == '__main__':
    #input
    #N,M
    N,M = map(int,sys.stdin.readline().rstrip().split())
    #grid
    # 0:empty, 1:house, 2:chicken
    grid = [[]]
    house_list = []
    chicken_list = []
    for r in range(N):
        row = list(map(int,sys.stdin.readline().rstrip().split()))
        for c,el in enumerate(row):
            if el == 1:
                house_list.append([1+r, 1+c])
            elif el == 2:
                chicken_list.append([1+r, 1+c])
        grid.append(row)
    C = len(chicken_list)

    if C == M:
        answer = get_city_chicken_distance(house_list, chicken_list)
        print(answer)
    else:
        combinations = list(combinations(chicken_list, M))
        dist_comparison_list = []
        for combination in combinations:
            dist_comparison_list.append(get_city_chicken_distance(house_list,combination))
        answer = min(dist_comparison_list)
        print(answer)