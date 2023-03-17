class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=[]
        if x<0:
            return False
        else:
            while x > 0:
                 num.append(x % 10)
                 x = (x - x %10)//10
            c=len(num)
            b=[]
            while c-1 >=0:
                b.append(num[c-1])
                c=c-1
            if num==b:
                return True
            else:
                return False