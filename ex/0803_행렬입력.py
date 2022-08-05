#1 2 3
#4 5 6
#7 8 9

# matrix =[]
# for i in range(3):
#     matrix.append(list(map(int, input().split())))
# print(matrix)


#list comprehension으로 해보기
#---

#N*M 행열
N, M = map(int, input().split())
# matrix = []
# for i in range(N):
#     matrix.append(list(map(int, input().split())))
# print(matrix)

matrix = [list(map(int, input().split())) for i in range(N)]
print(matrix)