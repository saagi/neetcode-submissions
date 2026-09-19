class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map={}
        for char in s:
            count_map[char]=count_map.get(char,0)+1
            # print(count_map)
        for char in t:
            if char not in count_map:
                return False
            count_map[char]-=1
            # print(count_map)
        for v in count_map.values():
            if v!=0:
                return False
        return True
        