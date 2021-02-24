#!/usr/bin/python3

#Given a string, find the length of the longest substring without repeating characters.

#Example 1:
#Input: "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#Example 2:
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.

#Example 3:
#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

#解题思路：滑动窗口
#滑动窗口的右边界不断的右移，只要没有重复的字符，就持续向右扩大窗口边界。一旦出现了重复字
#符，就需要缩小左边界，直到重复的字符移出了左边界，然后继续移动滑动窗口的右边界。以此类推，
#每次移动需要计算当前⻓度，并判断是否需要更新最大⻓度，最终最大的值就是题目中的所求。



#python中的方法和数据默认都是public类型的，此时方法和变量名前面都没有下划线
#public可以被子类，类内外访问
#_xx,以单下划线开头的是protected类型的变量或者方法，只允许本身以及子类访问
#__xx，以双下划线开头的是私有的变量或者方法，只允许类内访问
#__xx__是python的内置变量名
#判断两个对象的时候，类似于java的==号机制，py的__eq__方法也可以重写
#Python中没有数组的数据结构，但列表很像数组，如：a=[0,1,2]
#这时：a[0]=0, a[1]=1, a[[2]=2,但引出一个问题,即如果数组a想定义为0到999怎么办?这时可能通过a = range(0, 1000)实现。
# 或省略为a = range(1000).如果想定义1000长度的a,初始值全为0,则 a = [0 for x in range(0, 1000)]
#python中没有&&运算符，直接用英文表示了逻辑。and or
#python访问字符串：
#var1[0]:  H
#var2[1:5]:  ytho
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #如果长度是0，直接返回
        if len(s) == 0:
            return 0
        #定义一个定长256的数组，代表ascii码集合，其实128就够了
        freq = [0 for x in range(0, 255)]
        #结果，左，右
        result = 0
        left = 0
        right = -1
        #遍历整个字符串
        while left < len(s):
            #窗口开始滑动
            #如果右index+1小于长度，而且该字符的ascii码-a的ascii码位置上值为0，代码无重复。
            if right + 1 < len(s) and freq[ord(s[right + 1]) - ord('a')]== 0:
                #那么该位置+1
                freq[ord(s[right + 1]) - ord('a')] += 1
                #窗口右边进1
                right += 1
            else:
                #否则，该位置置为0
                freq[ord(s[left]) - ord('a')] -= 1
                #窗口左边进1
                left += 1
            #每滑动一次，比较一下最长长度。
            result = max(result, right - left + 1)
        #循环结束，返回值
        return result

    def max(a: int, b: int):
        if a > b:
            return a
        return b
class Main:
    list = Solution.lengthOfLongestSubstring(Solution(), 'pwwkew')
    print(list)
