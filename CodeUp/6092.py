# https://codeup.kr/problem.php?id=6092

n = int(input())
n_call = list(map(int,input().split()))
cnt = [0]*23


for nc in n_call:
    cnt[nc-1] += 1
for c in cnt:
    print(c, end=' ')




