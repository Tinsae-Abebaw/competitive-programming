class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        b=0
        new_array=[]
        boolean_return=[0]*len(l)
        for i in range(0,len(l)):
            new_array=nums[l[i]:r[i]+1]
            new_array.sort()
            b=new_array[1]-new_array[0]
            for j in range(0,len(new_array)-1):
                if b !=new_array[j+1]-new_array[j]:
                    boolean_return[i]=False
                    break
                elif b==new_array[j+1]-new_array[j] and j==len(new_array)-2:
                    boolean_return[i]=True
                    break
        return boolean_return