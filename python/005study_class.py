name = 'kookdonghun'
email = 'dh3978@naver.com'
addr = 'Ilsan'

def print_business_card(name, email, addr):
    print('-'*33)
    print(f'Name : {name}')
    print(f'E-mail : {email}')
    print(f'Address : {addr}')
    print('-'*33)

print_business_card(name,email,addr)

class BusinessCard:
    pass

card1 = BusinessCard()
print(card1) # <__main__.BusinessCard object at 0x0000028FDA504438> 객체의 메모리 주소 

