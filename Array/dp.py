#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:

    @staticmethod
    def dp_1(array, n):
        '''
        F[k] = max（F[i]+1| A[k] > A[i], 1 < i < k-1) (k>1)
        '''
        F = [1] * n
        maxLength = 1
        for i in range(1, n):
            # generate F[i] in every loop
            for j in range(i):
                if (array[i] > array[j]):
                    maxLength = max(maxLength, F[j] + 1)
            F[i] = maxLength
        return F[i]

    @staticmethod
    def dp_maxSubArray(array, n):
        '''
        dp(i) = max{(dp(i-1), sum}
        sum = sum + array[i])
        :param array:
        :return:
        '''
        dp = [0] * n
        dp[0] = array[0]
        sum = 0
        for i in range(1, n):
            sum = sum + array[i]
            dp[i] = max(dp[i-1], sum)
            if (sum < 0):
                sum = 0
        return dp[n-1]


if __name__ =='__main__':
    array = [1, 7, 2, 8, 3, 4]
    n = 6
    print Solution.dp_1(array, n)

    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = 9
    print Solution.dp_maxSubArray(array, n)