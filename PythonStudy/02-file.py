with open(r"test.txt", "r") as f:
    f.seek(2, 0) # seek移动单位是字节，一个汉字两个字节
    strChar = f.read()
    print(strChar)