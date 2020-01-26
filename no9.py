class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        l = len(x)
        for i in range(int(l/2)):
            if (x[i] == x[l-i-1]):
                continue
            else:
                return False
        return True
if __name__ == '__main__':
    answer = Solution()
    print(answer.isPalindrome(123421))
