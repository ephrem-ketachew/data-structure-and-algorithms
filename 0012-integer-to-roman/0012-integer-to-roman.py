class Solution:
    def intToRoman(self, num: int) -> str:
        to = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'
        }

        roman = ''
        temp = ''
        prev_len = len(str(num))
        while num > 0:
            cur_len = len(str(num))
            if cur_len != prev_len:
                roman += temp[::-1]
                temp = ''
                prev_len = cur_len

            tens = 10 ** (cur_len - 1)
            freq = num // tens
            if freq == 5:
                temp += to[tens * 5]
                num -= tens * 5
            elif freq == 4 or freq == 9:
                temp += to[tens * freq][::-1]
                num -= tens * freq
            else:
                temp += to[tens]
                num -= tens

        return roman + temp[::-1]