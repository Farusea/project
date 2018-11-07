class Solution:
    def lengthOflongestSubstring(self, s):
       temp = 0
       d = {}
       start = 0
       for i in range(len(s)):
           if s[i] in d and start <= d[s[i]]:
               start = d[s[i]] + 1

           temp = max(i-start+1, temp)
           d[s[i]] = i
       return temp

f = Solution()
print(f.lengthOflongestSubstring("abcabcbb"))