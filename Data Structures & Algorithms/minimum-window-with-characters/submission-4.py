class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        min_windowlen = float("inf")
        curr_windowlen=0
        dict_t = {}
        dict_s = {}
        for char in t:
            dict_t[char] = dict_t.get(char,0)+1
        required = len(dict_t)
        formed = 0
        print(dict_t)
        left=0
        for right in range(len(s)):
            dict_s[s[right]] = dict_s.get(s[right],0)+1
            if s[right] in dict_t and dict_s[s[right]]==dict_t[s[right]]:
                formed+=1
            # print(dict_s) 
            while required==formed:
                curr_windowlen = right-left+1
                if curr_windowlen<min_windowlen:
                    left_final = left
                    right_final = right
                    min_windowlen = curr_windowlen
                dict_s[s[left]]-=1
                if s[left] in dict_t and dict_s[s[left]]<dict_t[s[left]]:
                    formed-=1
                left+=1
                
        if min_windowlen!=float("inf"):
            return s[left_final:right_final+1]
        return ""

        