# https://codeup.kr/problem.php?id=6093

n = int(input())
call = list(map(int, input().split()))
for i in range(len(call)-1, -1, -1):
    print(call[i], end=' ')
#print(call[::-1])