class Solution:

    @staticmethod

    def nimberOf1Bits(num):
        count = 0
        while(num):
            if num & 1:
                count += 1
            num >>= 1
        return count

if __name__ == '__main__':
    num = 11
    print Solution.nimberOf1Bits(num)