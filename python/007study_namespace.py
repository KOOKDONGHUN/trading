class Stock:
    market = 'kospi'

print(dir())# // ['Stock', '__annotations__', '__builtins__', '__cached__', '__doc__',
            # //  '__file__', '__loader__', '__name__', '__package__', '__spec__']
            # Stock이 추가됐다

print(Stock) # <class '__main__.Stock'>

# 클래스가 정의되면 하나의 독립적인 네임스페이스가 생기고 클래스내에 정의된 변수나 메서드는 해당 네임스페이스 안에 파이썬 딕셔너리 타입으로 저장된다
print(Stock.market)

# 네임스페이스를 확인하는 방법
print(Stock.__dict__) # // {'__module__': '__main__', 'market': 'kospi', '__dict__': <attribute '__dict__' of 'Stock' objects>,
                      #//   '__weakref__': <attribute '__weakref__' of 'Stock' objects>, '__doc__': None}

s1 = Stock()
s2 = Stock()

print(id(s1)) # 2120139199496
print(id(s2)) # 2120139199560

print(s1.__dict__) # 비어있음
print(s2.__dict__) # 비어있음

s1.market = 'kosdaq'
print(s1.__dict__) # {'market': 'kosdaq'}

print(s2.__dict__) # 비어있음

print(s1.market) # kosdaq

# 인스턴스의 네임스페이스에 해당 이름이 없으면 클래스의 네임스페이스로 이동
print(s2.market) # kospi

