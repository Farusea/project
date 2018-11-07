# 暴力破解
class Sloution:
    def longestPalindrome(self, s):
        if not s or len(s) == 1:    # 判断字符串是否为空或者字符串的是否只有一个元素
            return s    # 结果返回字符串
        max_len = 0    # 设置最大长度
        result = ''    # 设置回文子串
        for i in range(len(s)):
            for j in range(i, len(s)):
                rst = s[i:j+1]      # 切片
                rrst = rst[::-1]    # 字符串逆置
                if rst == rrst and len(rst) > max_len:     # 判断是否为回文子串，并且长度是否大于之前的回文子串
                    max_len = len(rst)
                    result = rst       # 把回文子串赋给设定的变量
        print(result)
        return rst

s = "zsdasdasdfafasf"
f = Sloution()
f.longestPalindrome(s)