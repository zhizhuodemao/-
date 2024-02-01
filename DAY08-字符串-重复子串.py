'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。
'''
"""
思路 拼接在一起 如果出现s 就代表存在重复子串
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        ss = s[1:] + s[:-1]
        print(ss.find(s))
        return ss.find(s) != -1
