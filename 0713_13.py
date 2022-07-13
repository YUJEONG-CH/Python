#문제13. 문자열 조작하기 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
#input=apple outpu=elppa

#방법1
word='apple'
reword=''
for i in word:
    reword=i+reword
print(reword)



# 방법2
# word='apple'
# reword=word[::-1]
# print(reword)