# 第一种方法
class Solution:
    def isPalindrome(self, x):
        m = x
        temp = 0
        flag = isinstance(x, int) # 判断是否为整数
        if flag and x >= 0:
            for i in range(len(str(x))):
                temp = temp*10 + m%10  # 整数逆置
                m = m//10
            return flag if x == temp else False  # 三目运算
        else:
            return False


"""
时间太长
"""
# 第二种方法
class Solution2:
    def isPalindrome(self, x):
        flag = isinstance(x, int)
        if flag and x >= 0:
            x = str(x)
            rx = x[::-1]
            return flag if x == rx else False
        else:
            return False

x = 230
f = Solution()
print(f.isPalindrome(x))






