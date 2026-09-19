class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for element in nums:
            if element in hashmap:
                return True
            hashmap[element] = hashmap.get(element,0)+1
        return False
        