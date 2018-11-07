with open(r"test.txt", "w") as f:    # 以写方式创建一个文本文档
    # 将文本写入文件
    f.write("转眼之间离开你已过了这么多年\n如今才发现我一直在原地转圈\n远方有多遥远\n距离就像在两个世界\n爱是我们久违的诺言\n\n")
    f.close()
with open(r"test.txt", "r") as f:   # 以读的方式将文件按字符读出，设置参数以几个字符读取
    strChar = f.read(1)     # 一个字符一个字符的读取
    while strChar:  # 循环语句，当字符不为空时输出字符
        print(strChar)
        # print(len(strChar))   # 若读取整个文档，输出整个文档的字符个数
        strChar = f.read(1)     # 这个必须要有，否则在第一次读取字符时死循环
with open(r"test.txt", "a") as f:   # 以append（追加）方式在文档后面添加字符
    f.write("                  --不曾远走")
