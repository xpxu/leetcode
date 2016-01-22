class Solution(object):
    '''
    input: array
    output: length
    remove some element and return the length of array
    '''
    @staticmethod
    def remove_element_1(array, value):
        count = 0
        for i in array:
            if i == value:
                count = count + 1
        result = len(array) - count
        return result

    @staticmethod
    def remove_element_2(array, value):
        j = 0
        for i in range(len(array)):
            if array[i] != value:
                array[j] = array[i]
                j += 1
        return j

    @staticmethod
    def remove_Duplicates(array):
        '''
        :param array: a sorted array
        :return:
        '''
        j = 1
        for i in range(1, len(array)):
            if array[i] != array[i-1]:
                array[j] = array[i]
                j += 1
        return j


if __name__ == '__main__':
    array = [1, 3, 5, 6, 8, 0, 5, 6, 5]
    result1 = Solution.remove_element_1(array, 5)
    print result1
    result2 = Solution.remove_element_2(array, 5)
    print result2

    array = [1, 1, 2, 3, 5, 5, 6]
    result3 = Solution.remove_Duplicates(array)
    print result3