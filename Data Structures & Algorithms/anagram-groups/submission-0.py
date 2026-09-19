class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=defaultdict(list)
        result=[]
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-ord("a")]+=1
            hash_map[tuple(count)].append(s)
        for k,v in hash_map.items():
            result.append(v)
        return result

        