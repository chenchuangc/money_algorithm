class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        count = 0
        list = []
        list.append(n)
        while(count !=1):
            count = 0
            for i in s:
                a = int(i)
                b = a*a
                count = count + b
            if count ==1:
                return True
            elif count not in list:
                list.append(count)
                s = str(count)
            else:
                return False


if __name__ == '__main__':
    answer = Solution()
    print(answer.isHappy(1))