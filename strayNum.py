#Link:
#https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

def stray(arr):
	a,b = set(arr)
	if arr.count(a) > 1:
		return b
	return a