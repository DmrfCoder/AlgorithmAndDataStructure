class Solution:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        else:
            c=0
            a=1
            b=2
            for i in range(number-2):
                c=a+b
                a=b
                b=c
            return c


solution = Solution()
print solution.rectCover(3)

