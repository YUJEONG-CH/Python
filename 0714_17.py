# 문제 17. 소문자-대문자 변환하기
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# banana #BANANA
# 특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 ord 이다. ord('a') # 97
# 해당 유니코드 숫자를 문자로 반환하는 함수는 `chr`이다. chr(97) # 'a'



word='banana'
upword=''
for i in word:
    
    upword+=i

