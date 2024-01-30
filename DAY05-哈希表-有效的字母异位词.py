"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
示例 1: 输入: s = "anagram", t = "nagaram" 输出: true
示例 2: 输入: s = "rat", t = "car" 输出: false
说明: 你可以假设字符串只包含小写字母。
"""
"""
思路 判断S的每个字母是否在T中出现过
或者说 是否存在某个字符不在T中
"""
class Solution:
    """
    构建一个数组 该数组的长度为26位 是所有小写字母的长度
    s中的每一个字符 都会让对应位置加1 t中的每个字符都会让对应位置减一
    如果最后数组中存在1 就说明s中有些字母在t中没出现
    """
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True