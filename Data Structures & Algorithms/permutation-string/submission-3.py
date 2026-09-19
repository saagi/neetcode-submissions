class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hash = {}
        s2hash={}
        for item in s1:
            s1hash[item] = s1hash.get(item,0)+1#a:1,b:1
        size = len(s1)#2
        left=0
        for right in range(len(s2)):#right:0,1
            s2hash[s2[right]]=s2hash.get(s2[right],0)+1 #l:1,e:1
            if right-left+1==size:#F,T
                if s1hash==s2hash:
                    return True
                s2hash[s2[left]]-=1
                if s2hash[s2[left]]==0:
                    del s2hash[s2[left]]
                left+=1
        return False

        
        