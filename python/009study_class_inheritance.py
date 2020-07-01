class Parent:
     def can_sing(self):
         print('Sing a song')

father = Parent()
father.can_sing()

class LuckyChild(Parent):
    pass

ch1 = LuckyChild()
ch1.can_sing()

class UnLuckyChild():
    pass

ch2 = UnLuckyChild()
# ch2.can_sing() # AttributeError: 'UnLuckyChild' object has no attribute 'can_sing'

class LuckyChild2(Parent):
    def can_dance(self):
        print('Let`s dance ~')

ch3 = LuckyChild2()
