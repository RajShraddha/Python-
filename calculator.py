inp1 = int(input("enter a number:   "))

inp2= int(input("enter number 2:   "))










def add(inp1,inp2):
    return inp1+inp2

def sub(inp1,inp2):
    return inp1-inp2

def mul(inp1,inp2):
    return inp1*inp2

def divide(inp1,inp2):
    return inp1/inp2

def rem(inp1,inp2):
    return inp1%inp2

def calculate (choice):
    cal = {
       1: add,

      2: sub,

       3: mul,

       4: divide,

       5:rem
       }

    return cal.get(choice , lambda s,y:"invalid number")(inp1,inp2)


choice= int(input("enter choice:     "))

while True:
    print(calculate(choice))
    inp3 = input("do you want to continue, type yes  or no:    ")
    if(inp3=='yes'):
        inp1 = int(input("enter a number:   "))
        inp2= int(input("enter number 2:   "))
        choice= int(input("enter choice:     "))
        continue

        

       
        
        
    else:
        
        break
    



        





