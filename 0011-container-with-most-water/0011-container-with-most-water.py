class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma=0
        i=0
        j=len(height)-1
        while i<j:
            ma=max(ma,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
        return ma