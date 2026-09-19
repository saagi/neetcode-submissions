class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        hashmap={}
        maxlen=0 # AAABABB
        for right in range(len(s)):
            hashmap[s[right]]=hashmap.get(s[right],0)+1
            replaces = right-left+1-max(hashmap.values())#0
            while replaces>k:#F
                hashmap[s[left]]-=1
                if hashmap[s[left]]==0:
                    del hashmap[s[left]]
                left+=1
                replaces = right-left+1-max(hashmap.values())
            maxlen = max(maxlen,right-left+1)
        return maxlen
        