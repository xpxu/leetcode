class Solution:
    # @param height, a list of integer
    # @return an integer
    @staticmethod
    def largestRectangleArea(height):
        if not height:
            return 0
        if len(height) == 1:
            return height[0]
        stack = []  # The bottom element in the stack is the lowest
        max_area = 0
        n = len(height)
        for i in range(n + 1):
            # generate a max_area while meet the requirement.
            while stack and (i == n or height[stack[-1]] > height[i]):

                h = height[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                # When will the stack be empty?
                # We can notice that:
                # when stack is empty, the whole lenth i from zero is the w.
                # eg: 1 * 6, 1 * 2 when i = 1 and i =6
                    w = i
                    print 'i is %s' % i
                max_area = max(max_area, h * w)

            # append i into the stack
            stack.append(i)

        return max_area

    @staticmethod
    def listtest():
        testlist = [1, 2, 3]
        print testlist[-1]

if __name__ == '__main__':
    height = [2, 1, 5, 6, 2, 3]
    print Solution.largestRectangleArea(height)
