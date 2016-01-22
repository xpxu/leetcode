class Solution:

    @staticmethod
    def missingNumber(array):

        n = len(array)
        result_1 = 0
        result_2 = array[0]
        for i in range(1, n+1):
            result_1 = result_1 ^ i
        for i in range(n):
            result_2 = result_2 ^ array[i]

        return result_2 ^ result_1


if __name__ == '__main__':
    array = [0, 1, 3, 5, 4, 6, 2, 7, 9]
    print Solution.missingNumber(array)