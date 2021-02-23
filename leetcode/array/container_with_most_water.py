# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container,such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

#给出一个非负整数数组 a1，a2，a3，...... an，每个整数标识一个竖立在坐标轴 x 位置的一堵高度为 ai 的墙，选择两堵墙，和 x 轴构成的容器可以容纳最多的水。

#解题思路：滑动双指针
#分析:最开始想要使用双重for循环暴力破解，即循环每个边与其他边的所有面积，然后找到最大的面积。
#但这么做就发现又有一个问题：重复计算，效率很低
#经过画图观察，发现了一个规律，高度低的点对应比他高的最远点的面积最大，要想比这个面积更大，需要找高度高一些的中间点与远点的面积例如原来是1*8，后面可能出现2*7。
#找到这么一个点以后，发现这个点的高度比最远点都高，说明最远点再近一点有可能会超越现在的max。这里又一个规律是，只要点移动，并且比原来的点高1，面积一定会变大。
#那么开始移动最远点，远点要减一，减一以后要是比原最远点小的话，就继续，因为面积肯定变小了。直到遇到一个比前面的点高度高的，才有机会比原来的max大。
#到现在问题就变成了不断缩小宽度，来寻找一个高度，从而比宽度最大时的面积大的问题。
#通过双下标的夹逼来试出最大面积，在宽最大的情况下，缩小宽的过程中，只有找到了更长的高，才有机会击败最长宽时的面积。所以在这个过程中要不断地舍弃短高，只为找到一种可能性，同时不能放弃已找到的最大值。
from typing import List


class Solution:
    # :和->分别是参数建议类型和返回值建议类型
    # python的_init_是构造函数
    # python的层与层之间空四个开头
    def maxArea(height: List[int]) -> int:
        # 定义双指针start，end
        max = 0
        start = 0
        end = len(height) - 1
        # start与end的下标框出范围
        while start < end:
            #start与end框出宽度
            width = end - start
            high = 0
            #找到最低的高度
            if height[start] < height[end]:
                high = height[start]
                start += 1
            else:
                high = height[end]
                end -= 1
            #取面积最大值
            temp = width * high
            if temp > max:
                max = temp
        #循环结束就返回
        return max


class Main:
    max = Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(max)