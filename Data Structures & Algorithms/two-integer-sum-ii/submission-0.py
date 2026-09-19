class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_map={}
        for index,val in enumerate(numbers):
            lookup = target-val
            if lookup in dict_map:
                return [dict_map[lookup]+1,index+1]
            dict_map[val]=index
        return [-1,-1]
        