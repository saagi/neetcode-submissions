class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        hashmap={}
        maxlen=0
        for right in range(len(s)):
            hashmap[s[right]]=hashmap.get(s[right],0)+1
            while hashmap[s[right]]!=1:
                hashmap[s[left]]-=1
                left+=1
            maxlen = max(maxlen,right-left+1)
        return maxlen
        