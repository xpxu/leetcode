class Solution:
    '''
    if a num is a power of two, it only have one or zero 1 in its
    binary format
    '''
    @staticmethod
    def isPowerOfTwo(num):

        if num < 0:
            return False
        hasOne = False
        while(num):
            if (num & 1):
                if hasOne :
                    return False
                else:
                    hasOne = True
            num >>= 1
        return True


if __name__ == '__main__':
    num = 10
    print Solution.isPowerOfTwo(num)