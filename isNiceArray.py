#Link:
#https://www.codewars.com/kata/59b844528bcb7735560000a0/train/python

def is_nice(arr):
	print(arr)
	if arr:
		for first in arr:
			if first + 1 in arr or first - 1 in arr:
				pass
			else:
				return False
		return True
	return False
