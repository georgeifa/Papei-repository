#functions for the numbers
def zero():
        x = 0
        return int(x)
def one():
        x=1
        return int(x)
def two():
        x=2
        return int(x)
def three():
        x=3
        return int(x)
def four():
        x=4
        return int(x)
def five():
        x=5
        return int(x)
def six():
        x=6
        return int(x)
def seven():
        x=7
        return int(x)
def eight():
        x=8
        return int(x)
def nine():
        x=9
        return int(x)
#functions for the calculations
def plus(z,y):
    print z + y

def times(z,y):
    print z * y

def minus(z,y):
    print z - y

t1 = raw_input("Insert your text:  ")
#split ragarding ( because the there enters the next function
t2 = t1.split("(")
#list with name of number functions
t3=['zero','one','two','three','four','five','six','seven','eight','nine']
t4=[zero(),one(),two(),three(),four(),five(),six(),seven(),eight(),nine()]
for i in range(0,10):
    #if the the first cell in t2 (the list with the splits) is the same with the number in cell i of t3 (the list with the numbers)
    if (t3[i] == t2[0]):
        a=t4[i]

for i in range(0,10):
    #if the the third cell in t2 (the list with the splits) is the same with the number in cell i of t3 (the list with the numbers)
    if (t3[i] == t2[2]):
        b=t4[i]
#do the calculation which is written in the second cell of t2(the list with the splits)
if (t2[1] == 'plus'):
     plus(a,b)
elif (t2[1] == 'times'):
     times(a,b)
elif (t2[1] == 'minus'):
     minus(a,b)
