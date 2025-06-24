class Calc():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def dlg(self):
        return self.a/self.b
    
p1 = Calc(1,0)
print(p1.dlg)