class Solution:
    def myAtoi(self,str):
        import re
        s = re.findall(r'  \d+', str.strip())




f = Solution()
print(f.myAtoi(""))

# ValueError: invalid literal for int() with base 10: ''  这个错误要把人整疯！！