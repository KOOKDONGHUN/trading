print(abs(-3)) # 3 실수 혹은 정수를 입력받아 절댓값을 반환해주는 내장함수

print(abs(-3.0)) # 3.0

try : 
    print(abs('hello')) # TypeError: bad operand type for abs(): 'str'
except :
    print('TypeError: bad operand type for abs(): \'str\'')

print(chr(97)) # a 유니코드 값을 입력받은 후 그 값에 해당하는 문자열을 반환합니다.
print(chr(65)) # A

for i, stock in enumerate(['Naver', 'KAKAO', 'SK']): # 리스트 자료형은 인덱스를 값으로 반환하지 많으므로 인덱스 값을 같이 반환해주는 내장함수
    print(i, stock)
'''
0 Naver
1 KAKAO
2 SK    '''

# 해당 객체의 고윳값을 반환한다? 객체가 할당된 메모리의 주솟값을 말한다.
a = 1
b = 2
print(id(a)) # 140735116668672
print(id(b)) # 140735116668704

print(len({1: 'SK', 2:'Naver'})) # 리스트, 튜플, 문자열, 딕셔너리의 원소의 개수를 반환한다.

print(list('hello')) # ['h', 'e', 'l', 'l', 'o']

print(list((1,2,3))) # [1, 2, 3] 튜플을 리스트로 변환함

print(max(1,2,3)) # 3 입력값중 최댓값을 반환한다

print(sorted((4,3,1,0))) # [0, 1, 3, 4] // 입력값을 정렬한 후 결과값을 리스트로 반환한다.
print(sorted(['c', 'b', 'a'])) # ['a', 'b', 'c']