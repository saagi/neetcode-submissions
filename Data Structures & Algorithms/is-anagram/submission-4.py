class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            count_map[s[i]]=count_map.get(s[i],0)+1
            count_map[t[i]]=count_map.get(t[i],0)-1
        return not any(count_map.values())
        # count_map={}
        # for char in s:
        #     count_map[char]=count_map.get(char,0)+1
        #     # print(count_map)
        # for char in t:
        #     if char not in count_map:
        #         return False
        #     count_map[char]-=1
        #     # print(count_map)
        # for v in count_map.values():
        #     if v!=0:
        #         return False
        # return True
        