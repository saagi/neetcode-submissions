class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        lp = 0
        rp = len(heights)-1
        while lp<=rp:
            area = (rp-lp)*min(heights[rp],heights[lp])
            if area>max_area:
                max_area=area
            if heights[lp]<heights[rp]:
                lp+=1
            else:
                rp-=1
        return max_area
        
        