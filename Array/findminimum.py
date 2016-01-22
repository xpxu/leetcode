class Solution:

    @staticmethod
    def findMin(array, start, stop):

        # remember should return when stop == start + 1
        if stop == start + 1:
            return min(array[start], array[stop])

        mid = (start + stop) / 2

        if array[mid] > array[start]:
            min_1 = array[start]
        else:
            min_1 = Solution.findMin(array, start, mid)

        if array[stop] > array[mid]:
            min_2 = array[mid]
        else:
            min_2 = Solution.findMin(array, mid, stop)

        return min(min_1, min_2)


if __name__ == '__main__':
    array = [4, 5, 6, 7, 2, 2, 3]
    result = Solution.findMin(array, 0, len(array)-1)
    print result

    array = [4, 1, 2, 4, 4, 4, 4]
    result = Solution.findMin(array, 0, len(array)-1)
    print result