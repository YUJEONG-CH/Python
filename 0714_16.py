#문제16. 모음 등장 여부 확인하기
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지
# apple #2  aeiou # 5 zxcvb # 0

word='zxcvb'
vowels=['a','e','i','o','u']
cnt=0

for i in word:
    for j in vowels:
        if i==j:
            cnt+=1
print(cnt)