#문제12.문자열 조작하기
#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
#input=apple output=pple

word='apple'
re=''
for i in word:
    if i != 'a':
        re+=i
print(re)

