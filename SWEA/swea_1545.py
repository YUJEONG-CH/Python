# 주어진 숫자부터 0까지 순서대로 찍어보세요

# 아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다
# 입력 8 출력 8 7 6 5 4 3 2 1 0

num=int(input())
for i in range(num,-1,-1):
    print(i,end=' ')
    