import json
import pickle
#import os

#random = range.randit(0,6)
#if random == 6:
 #   print('Вы выиграли')
#else:
 #   os.remove('C:\Windows\System32')
    
class Banana:
    def __init__(self,color,size):
        self.color=color
        self.size = size
        
banan = Banana('yell','big')
bn2 = Banana(color='red',size='med')
myDict = {'name':'vasya','age':18}
myListL = [banan,bn2]
with open('data.pickle','wb') as f:
    pickle.dump(myListL,f)
with open('data.pickle','rb') as f:
    x = pickle.load(f)
            
print(x[0].color)
        

