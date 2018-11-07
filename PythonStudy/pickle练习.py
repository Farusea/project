# pickle序列化，把程序运行中的信息保存在磁盘上
# 反序列化：序列化的逆反过程
# pickle:Python提供的序列化模块
# pickle.dump:序列化
# pickle.load:反序列化

import pickle
txt = "这只是一个测试文件！"
with open(r'test01.txt', 'wb') as f:
    pickle.dump(txt, f)  # 序列化

with open(r'test01.txt', 'rb') as f:
    txt = pickle.load(f) # 反序列化
    print(txt)