# https://www.acmicpc.net/problem/10871

N, X = map(int, input().split())
list_ = []
list_ = list(map(int, input().split()))
for l in list_:
    if l < X:
        print(l, end=' ')