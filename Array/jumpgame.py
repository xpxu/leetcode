class Solution:

    @staticmethod
    def jumpGame(array):

        maxposition = array[0]

        if len(array) == 1:
            return True
        for i in range(1, len(array)):
            maxposition = max(maxposition, i + array[i])
            if maxposition >= len(array)-1:
                return True
            if maxposition == i:
                return False

    @staticmethod
    '''
    Dynamic program for minimum step
    '''
    def jumpGame_2(array):

        step = [0] * len(array)
        for k in range(1, len(array)):
            for j in range(k):
                if array[j] >= k -j:
                    step[k] = step[j] + 1
                    break

        return step[len(array) - 1]


if __name__ == '__main__':
    array = [2, 3, 1, 1, 4]
    print Solution.jumpGame(array)
    array = [2, 3, 1, 1, 4]
    print Solution.jumpGame_2(array)