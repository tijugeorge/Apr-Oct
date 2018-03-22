def divide(dividend, divisor):
	neg = ((dividend < 0) != (divisor < 0))
	dividend = left = abs(dividend)
	divisor = div = abs(divisor)
	if dividend < divisor:
		return 0
	Q = 1
	ans = 0
	while left >= div:
		left -= div
		ans += Q
		Q += Q
		div += div
	if neg:
		return max(-(ans+divide(left, divisor)), -2147483648)
	else:
		return min(ans + divide(left, divisor), 2147483648)


print(divide(21, 7))
print(divide(21, 3))
print(divide(-28, 2))
