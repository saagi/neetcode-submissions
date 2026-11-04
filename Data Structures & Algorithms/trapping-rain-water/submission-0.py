class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        lmax = 0
        r=len(height)-1
        rmax = len(height)-1
        total=0

        while l<=r:
            if height[lmax]<=height[rmax]:
                if height[l]<=height[lmax]:
                    total+=height[lmax]-height[l]
                else:
                    lmax = l
                l+=1
            else:
                if height[r]<=height[rmax]:
                    total+=height[rmax]-height[r]
                else:
                    rmax = r
                r-=1
        return total

        