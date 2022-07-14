#문제15. 문자의 위치 구하기
# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지
# input=banana #1 apple # 0 kiwi # -1
#--------------------------------------------------------------------------------------------------

# word='banana'
# index=0
# for i in word:
#     if i=='a':
#         print(index)
#         break 
#     index+=1
# if word[index-1]!='a':
#     print(-1)
    

#추가문제
#문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
#find() index() 메서드 사용 금지    
#HappyHacking #1 6  banana # 1 3 5 kiwi # 

word='HappyHacking'
index=0
for i in word:
    if i=='a':
        print(index, end=' ') 
        
    index+=1
