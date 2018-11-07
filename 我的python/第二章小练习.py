# 捕获异常
def _pay():
    try:
        Hours = float(input("Enter Hours:"))
        Rate = float(input("Enter Rate:"))

        if Hours > 40:
            pay = (Hours-40)*1.5*Rate+40*Rate
            print(pay)
        else:
            print(Hours*Rate)
    except:
        print("Please enter number!")
        _pay()


# 综合应用小代码
def _socre():
    try:
        socre = float(input("输入你的分数（0.0~1.0之间）："))
        if socre >= 0 and socre <= 1:
            if socre >= 0.9 and socre <= 1.0:
                print("A")
            elif socre >= 0.8:
                print("B")
            elif socre >= 0.7:
                print("C")
            elif socre >= 0.6:
                print("D")
            else:
                print("F")
        else:
            print("Error")
    except ValueError:
        print("请输入有效值（0.0~1.0）!")

    finally:
        _socre()

_socre()