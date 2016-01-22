class Solution:
    @staticmethod
    def plusOne(digitArray):
        tmpDigit = 0
        for i in range(len(digitArray)-1, -1, -1):
           tmpDigit = digitArray[i]
           digitArray[i] = (tmpDigit + 1) % 10
           tmpDigit = (tmpDigit + 1) / 10
           if not tmpDigit:
               break
        if tmpDigit:
            digitArray.insert(0, 1)
        return digitArray


if __name__ == '__main__':
    digitArray = [9, 9, 9, 9]
    print Solution.plusOne(digitArray)

