class Solution:

    @staticmethod
    def isPalindorme(num):

        if num < 0:
            return False
        elif num == 0:
            return True
        else:
            tmp = num
            palidormedNum = 0
            while(num):
                # remainer should be caculated first
                remainder = num % 10
                num = num / 10
                palidormedNum = palidormedNum*10 + remainder
            if palidormedNum == tmp:
                return True

if __name__ == '__main__':
    num = 12821
    print Solution.isPalindorme(num)