import sys

## input
N = int(sys.stdin.readline())
A_list = list(map(int,sys.stdin.readline().rstrip().split()))
B,C = map(int,sys.stdin.readline().rstrip().split())

ret = N

for i in range(N):
    if A_list[i] > B:
        A_list[i] = A_list[i] -B
    else:
        A_list[i] = 0

for a in A_list:
    if a%C == 0:
        ret += a//C
    else:
        ret += (a//C + 1)

print(ret)

# print(N)
# print(A_list)
# print(B,C)