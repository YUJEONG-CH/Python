# https://www.acmicpc.net/problem/10818

N = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))