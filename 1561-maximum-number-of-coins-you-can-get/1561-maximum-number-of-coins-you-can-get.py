class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=0
        j=len(piles)-1
        total=0
        while j>i:
            total+=piles[j-1]
            j-=2
            i+=1
        return total