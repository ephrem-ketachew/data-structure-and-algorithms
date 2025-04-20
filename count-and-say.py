class Solution:
    def countAndSay(self, n: int) -> str:
        def runLengthEncoding(string):
            encodedString = ''
            i = 0
            while i < len(string):
                count = 1
                j = i + 1
                while j < len(string) and string[i] == string[j]:
                    count += 1
                    j += 1
                encodedString += str(count) + string[i]
                if j < len(string):
                    i = j
                else:
                    break
            return encodedString
        if n == 1 :
                return "1"
        else:
            return runLengthEncoding(self.countAndSay(n - 1))