def countSymmetricIntegers(low,high):
    def sumOfDigits(n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s
    
    if high < 1000:
        if low < 100:
            total = 0
            for n in range(low, high + 1):
                if n > 99:
                    break
                if n % 11 == 0:
                    total += 1
            return total
    
        else:
            return 0

    else:
        leftMin = leftMax = rightMin = rightMax = rightMax1 = rightMax2 = rightMin1 = rightMin2 = -1
        leftMax = high // 100
        if low >= 1000:
            leftMin = low // 100
            if high - low > 99:
                rightMin = 0
                rightMax = 99
            elif high % 100 - low % 100 > 0:
                rightMin = low % 100
                rightMax = high % 100
            else:
                rightMin1 = 0
                rightMax1 = high % 100
                rightMin2 = low % 100
                rightMax2 = 99
        else:
            leftMin = 10
            rightMin = 0
            if high - 1000 > 99:
                rightMax = 99
            else:
                rightMax = high % 100
        

        pairs = {}
        for n in range(leftMin, leftMax + 1):
            s = sumOfDigits(n)
            if s in pairs:
                pairs[s][0] += 1
            else:
                pairs[s] = [1,0]

        if rightMax >= 0:
            for n in range(rightMin, rightMax + 1):
                s = sumOfDigits(n)
                if s in pairs:
                    pairs[s][1] += 1

        else:
            for n in range(rightMin1, rightMax1 + 1):
                s = sumOfDigits(n)
                if s in pairs:
                    pairs[s][1] += 1
            for n in range(rightMin2, rightMax2 + 1):
                s = sumOfDigits(n)
                if s in pairs:
                    pairs[s][1] += 1

        total = 0
        if low < 100:
            for n in range(low, 100):
                if n % 11 == 0:
                    total += 1

        for digitSum in pairs:
            total += pairs[digitSum][0] * pairs[digitSum][1]

        if rightMax == 99 or rightMax2 == 99:
            edge = sumOfDigits(leftMax)
            for n in range(high % 100 + 1, 100):
                s = sumOfDigits(n)
                if s == edge:
                    total -= 1

    return total