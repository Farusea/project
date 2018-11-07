def hello():
    name = input("Enter your name:")
    print("Hello {0}".format(name))

def _pay():
    Hours = int(input("Enter Hours:"))
    Rate = float(input("Enter Rate:"))
    pay = Hours*Rate
    print(pay)

def _type():
    width = 17
    height = 12.0
    A, B, C, D = width/2, width/2.0, height/3, 1+2*5
    print(A, B, C, D)
    print(type(A), type(B), type(C), type(D))

def warm():
    C = float(input("Enter 摄氏度;"))
    F = C*1.8+32
    print("当前摄氏度为{0}，转换成华氏度后是{1}".format(C, F))
