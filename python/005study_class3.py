name = 'kookdonghun'
email = 'dh3978@naver.com'
addr = 'Ilsan'

class BusinessCard:
    
    def set_info(self, name, email, addr): # self를 쓰는 이유 일단은 반드시 함수의 첫번째 파라미터는 self를 써야한다 책에서 일단은 외우란다.
        self.name = name
        self.email = email
        self.addr = addr
    
    def print_info(self):
        print('-'*33)
        print(f'Name : {self.name}')
        print(f'E-mail : {self.email}')
        print(f'Address : {self.addr}')
        print('-'*33)

member1 = BusinessCard()
member1.set_info(name, email, addr)
member1.print_info()

member2 = BusinessCard()
member2.set_info('dongkeun', 'donkeun@nate.com', 'Ilsan')
member2.print_info()

