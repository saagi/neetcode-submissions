class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_map={}
        for index,num in enumerate(nums):
            if target-num in dict_map:
                return [dict_map[target-num],index]
            dict_map[num]=index

        