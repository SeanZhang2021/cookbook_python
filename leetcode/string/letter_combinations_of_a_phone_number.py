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
# ""里面的‘’不需要显示声明转义字符，而‘’里面需要声明转义字符，其他时候一样
# example:  '\'A\'' |  "'A'"
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
    # list,map声明和访问数据的方式
    letterDict = [
        "", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    ]
    # 声明一个结果集
    res = []

    # 寻找字符组合
    # 先具体，后一般，如果只有两个
    # 基本思路是循环多次，从第一个字符串中找到所有的字符，循环遍历再循环第二个字符串，找到所有的字符，组合
    # 然后再开始循环第二个字符串，再循环第一个，组合
    # 发现，两次操作是一样的，能不能抽象出一个方法，传进来一个字符串，就能一个一个处理里面的字符和其他数字字符的组合
    # 所以，可以将第一个字符看作是空的和第一个字符的组合，这是起始态,要是找到了这个组合，那就存起来
    # 递归是一种解决方式，递归是单线程的，但是它能增加无数个调用栈，也就是原来传参数，现在调了个方法，要是不返回会一直调用这个方法就会一直调用，所以需要退出

    # 经过一段思考，发现，这其实是个n乘n乘n的问题，也就是树状结构，每一条路的组合构成了一个结果。所以遍历树
    # 即可得出结论。递归遍历树，每进入一层就传入上一层的结果，直到最后一层叶子节点，记录结果，
    # n*n*n的问题都可以归结于树的分叉遍历问题，用树来组织各种情况。
    def findCombinations(self, digits: list, index: int, s: str):
        if index == len(digits):
            # list添加新元素是append而不是add
            self.res.append(s)
            return
        num = digits[index]
        # 强制类型转换，也可以用ord('2')-ord('0')
        letter = self.letterDict[int(num)]
        # for循环两种形式：for i in range（数字）
        # for i in list
        # for i in str
        for i in range(len(letter)):
            # for循环中的递归，一下递归n个
            # 参数1:数字list，参数2:第几个数字，参数三当前值
            self.findCombinations(digits, index + 1, s + letter[i])
        return

    def letterCombinations(self, digits: str) -> list:
        if digits == "":
            return list
        self.findCombinations(digits, 0, "")
        return self.res

class Main:
    list = Solution.letterCombinations(Solution(), '234')
    print(list)
