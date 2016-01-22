class Solution:

    @staticmethod
    def pascalTriangle(n):
        triangle = []

        if n == 0:
            return

        for i in range(n):
            # first generate iList for i level
            if i == 0:
                iList = [1]
            elif i == 1:
                iList = [1, 1]
            else:
                iList = []
                iList.append(1)
                for j in range(1, i):
                    jNum = triangle[i - 1][j - 1] + triangle[i - 1][j]
                    iList.append(jNum)
                iList.append(1)

            # assign iList to triangle[i]
            triangle.append(iList)

        return triangle

    @staticmethod
    def pascalTriangle_2(n):
        nList = [1] * n

        if n < 3:
            return nList

        for i in range(2, n):
            # generate iList for ith loop
            for j in range(i-1, 0, -1):
                nList[j] =  nList[j] + nList[j-1]

        return nList

if __name__ == '__main__':
    n = 5
    print Solution.pascalTriangle(n)
    print Solution.pascalTriangle_2(n)