class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:      
        be={}
        for i, go in enumerate(nums):
            const=target-go
            if const in be:
                    return([be[const],i])
            elif go not in be:
                    be[go]=i