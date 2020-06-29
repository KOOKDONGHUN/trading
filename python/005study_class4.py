class Myclass:
    def __init__(self): # 생성자 // 객체의 생성과 동시에 자동으로 호출되는 메서드이다 // initialize의 약어 (초기화하다)
        print('create object!!')

inst1 = Myclass() # create object!!

name = 'kookdonghun'
email = 'dh3978@naver.com'
addr = 'Ilsan'

class BusinessCard:
    
    def __init__(self, name, email, addr): # self를 쓰는 이유 일단은 반드시 함수의 첫번째 파라미터는 self를 써야한다 책에서 일단은 외우란다.
        self.name = name
        self.email = email
        self.addr = addr
    
    def print_info(self):
        print('-'*33)
        print(f'Name : {self.name}')
        print(f'E-mail : {self.email}')
        print(f'Address : {self.addr}')
        print('-'*33)

try :
    member1 = BusinessCard() # TypeError: __init__() missing 3 required positional arguments: 'name', 'email', and 'addr'
except :
    print('TypeError: __init__() missing 3 required positional arguments: \'name\', \'email\', and \'addr\'')

member1 = BusinessCard(name, email, addr)
member1.print_info()