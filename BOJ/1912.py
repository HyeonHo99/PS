import sys

if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int,sys.stdin.readline().rstrip().split()))

    answer_list = [None for _ in range(n)]
    if num_list[n-1] > 0:
        answer_list[n-1] = num_list[n-1]
    else:
        answer_list[n-1] = 0

    for i in range(n-2,-1,-1):
        if (num_list[i] + answer_list[i+1]) > 0:
            answer_list[i] = num_list[i] + answer_list[i+1]
        else:
            answer_list[i] = 0

    if max(answer_list) == 0:
        answer = max(num_list)
    else:
        answer = max(answer_list)
    print(answer)
