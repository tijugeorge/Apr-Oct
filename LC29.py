#29. Divide Two Integers
def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    neg = ((dividend < 0) != (divisor < 0))
    dividend = left = abs(dividend)
    divisor = div = abs(divisor)
    Q = 1
    ans = 0
    while left >= divisor:
        left -= div
        ans += Q
        Q += Q
        div += div
        if left < div:
            div = divisor
            Q = 1
    if neg:
        #print(neg)
        return max(-ans, -2147483648)
    else:
        return min(ans, 2147483648)


print(divide(21, 7))
print(divide(21, 3))
print(divide(-28, 2))
