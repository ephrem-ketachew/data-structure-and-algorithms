import math as m
MAX_INTEGER =  int(m.pow(2, 31) - 1)
MIN_INTEGER = int(-m.pow(2, 31)) 

# def divide( dividend,  divisor):
#     if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
#         sign = 1
#     else:
#         sign  = -1
#     dividend = abs(dividend)
#     divisor = abs(divisor)
#     if dividend != 0:
#         quotient = 0
#         sum = divisor
#         while sum <= dividend:
#             sum += divisor
#             quotient += 1
#         quotient = sign * quotient
#         if quotient > MAX_INTEGER:
#             return MAX_INTEGER
#         elif quotient < MIN_INTEGER:
#             return MIN_INTEGER
#         else:
#             return quotient
#     else:
#         return 0

# print(divide(1, 1))

# def divide( dividend,  divisor):
#     if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
#         sign = 1
#     else:
#         sign  = -1
#     if dividend != 0:
#         quotient = m.exp(m.log(abs(dividend))-m.log(abs(divisor)))
#         quotient = sign * m.trunc(quotient)
#         if quotient > MAX_INTEGER:
#             return MAX_INTEGER
#         elif quotient < MIN_INTEGER:
#             return MIN_INTEGER
#         else:
#             return quotient
#     else:
#         return 0

# print(divide(231, 3))