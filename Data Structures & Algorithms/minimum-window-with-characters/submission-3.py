class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        minwindowsize = float("inf")
        minleft=0
        minright=0
        left=0
        thash = {}#XYZ x:1y:1z:1
        shash={}#OUZODYXAZV
        for item in range(len(t)):
            thash[t[item]]=thash.get(t[item],0)+1
        required = len(thash)#3
        formed=0
        for right in range(len(s)):
            shash[s[right]]=shash.get(s[right],0)+1#O:2U:1Z:1D:1Y:1X:1
            if s[right] in thash and thash[s[right]]==shash[s[right]]:
                formed+=1#formed=1,2,3
            while formed==required:#F,F,T,F
                currwindowsize = right-left+1
                if currwindowsize<minwindowsize:
                    minleft = left#0,2
                    minright=right#6
                    minwindowsize = currwindowsize
                shash[s[left]]-=1#O:0U:0Z:0D:1Y:1X:1
                if s[left] in thash and shash[s[left]]<thash[s[left]]:#True
                    formed-=1#2
                left+=1#3
        if minwindowsize==float("inf"):
            return ""
        return s[minleft:minright+1]


        