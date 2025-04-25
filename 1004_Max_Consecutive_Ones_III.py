class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        max_cnt = 0
        cnt = 0
        while j < len(nums):
            if nums[j] == 1:
                cnt += 1
                j+=1
            elif k > 0:
                cnt +=1
                k -= 1
                j +=1
            elif k == 0:
                max_cnt = max(max_cnt, cnt)
                while k == 0 and i <= j:
                    if nums[i] == 0:
                        k +=1
                    i += 1
                    cnt -=1

        max_cnt = max(max_cnt, cnt)
        return max_cnt

        

