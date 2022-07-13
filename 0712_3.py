# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지
# n=10

n=int(input())
sum=0
#1) while문
#while 

#2)for문
for i in range(n+1):
    sum+=i
print(sum)