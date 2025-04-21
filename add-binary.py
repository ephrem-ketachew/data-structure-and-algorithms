def addBinary(a, b):
    zeros = max(len(a), len(b))
    a = a.zfill(zeros)
    b = b.zfill(zeros)
    c = ''
    c.zfill(zeros)
    carry = 0
    for i in range(len(a) -1, -1, -1):
        num1 = int(a[i])
        num2 = int(b[i])
        result = (num1 + num2 + carry) % 2
        carry = (num1 + num2 + carry) //2
        c += str(result)
    if carry:
        c += str(carry) 
    return ''.join(reversed(c))