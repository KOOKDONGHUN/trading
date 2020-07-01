class Foo:
    def func1(): # self
        print('function 1!!')
    
    def func2(self):
        print(id(self))
        print('function 2!!')

f = Foo()
f.func2() # function 2!!

# f.func1() # 에러가 남 // 메소드를 호출할때는 항상 인스턴스(self)를 전달하는데 func1에는 파라미터가 없는데 억지로 인스턴스를 쑤셔넣을라니까 에러난다.
print(id(f))

f.func2()
