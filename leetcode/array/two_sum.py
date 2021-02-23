#!/usr/bin/python3

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 "和为目标值" 的那 "两个" 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 你可以按任意顺序返回答案。

# 示例 1：

# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：

# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：

# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#

# 提示：
# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案

from typing import List


class Solution:
    # :和->分别是参数建议类型和返回值建议类型
    # python的_init_是构造函数
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 定义字典
        keyMap = {}
        length = len(nums)
        #range是python的内置函数，可以框出一个范围(要头不要尾)，循环中常用
        for index in range(0, length):
            another = target - nums[index]
            # if another in keyMap:
            if keyMap.__contains__(another):
                # 找到了就返回
                return [index, keyMap[another]]
            # map记录数组中每个元素的值和index，便于后面查找，这样就能做到只遍历一次
            keyMap[nums[index]] = index
        # 整体没找到就返回空
        return


class Main:
    list = Solution.twoSum(Solution(), [3,3],6)
    print(list)