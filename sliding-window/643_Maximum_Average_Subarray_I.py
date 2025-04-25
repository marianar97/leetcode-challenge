# 643. Maximum Average Subarray I

# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0
        sum_val = 0
        max_avg = float('-inf')  # changed from 0 to handle negative numbers

        while j < len(nums):
            sum_val += nums[j]

            if (j - i + 1) < k:
                j += 1
            elif (j - i + 1) == k:
                max_avg = max(max_avg, sum_val / k)
                sum_val -= nums[i]
                i += 1
                j += 1

        return max_avg