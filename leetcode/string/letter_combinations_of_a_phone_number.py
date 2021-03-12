#!/usr/bin/python3
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
 #A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# 
#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#Note:
#Although the above answer is in lexicographical order, your answer could be in any order you want.

#python小技巧：
## 类变量
#class Man:  # 类变量
#    country = "中国"
#    def __init__(self, name, place):
#        self.name = name
#        self.place = place
#    def myself(self):
#        print("我来自%s，我叫%s" % (self.place, self.name))
#man1 = Man("吕子乔"， "四川省")
#man1.myself()

class Solution:
    staticName = 'zhangxiang'
    def __init__(self,name,place) -> None:
        self.name = name
        self.place = place

    def letterCombinations(self, s: str) -> int:
        return len(self.name)

    def findCombinations(self, digits:str,index:int,s:str)->int:
        return 1

class Main:
    list = Solution.letterCombinations(Solution('tt','ttt'), 'abcabcbb')
    print(list)
    print(Solution.staticName)