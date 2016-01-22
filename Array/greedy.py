class Solution(object):

    @staticmethod
    def maxWater(array):

        start = 0
        stop = len(array) - 1
        maxarea = 0

        while(start <= stop):
            area = (stop - start + 1) * min(array[start], array[stop])
            if array[start] <= array[stop]:
                start += 1
            else:
                stop -= 1
            maxarea = max(maxarea, area)
            print area

        return maxarea


if __name__ == '__main__':
    array = [2, 1, 5, 6, 2, 3]
    print Solution.maxWater(array)