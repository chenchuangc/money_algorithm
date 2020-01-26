class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'0':4,'1':9,                      '2':40,'3':90,'4':400,'5':900}

        s = s.replace('IV','0')
        s = s.replace('IX','1')
        s = s.replace('XL','2')
        s = s.replace('XC','3')
        s = s.replace('CD','4')
        s = s.replace('CM','5')
        # print(s)
        count = 0
        for i in s:
            count = count + roman[i]
        return count

if __name__ == '__main__':
    answer = Solution()
    print(answer.romanToInt('IV'))