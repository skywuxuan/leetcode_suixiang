#!/mnt/lustre02/jiangsu/aispeech/home/xmw01/tools/anaconda3/bin/python
# -*- coding: UTF-8 -*-

from typing import List

"""
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

示例 1：

输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
示例 2：

输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。
提示：

0 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        result = 1
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            if result < dp[i]:
                result = dp[i]

        return result

if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    solution = Solution()

    result =  solution.findLengthOfLCIS(nums)
    print(result)