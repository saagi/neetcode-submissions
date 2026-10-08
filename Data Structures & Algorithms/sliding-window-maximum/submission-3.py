import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        left=0
        windowmax=float("-inf") #[1,-1]
        # maxheap=[]
        if k==1:
            return nums
        for right in range(len(nums)):#[7,2,4], 2
            if nums[right]>windowmax:
                windowmax=nums[right]
            if right-left+1==k:
                output.append(windowmax)
                if windowmax==nums[left] and right+1<len(nums):
                    windowmax = max(nums[left+1:right+1])
                left+=1
        return output
        