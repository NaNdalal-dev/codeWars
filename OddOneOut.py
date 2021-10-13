#Link
#https://www.codewars.com/kata/5d376cdc9bcee7001fcb84c0/train/python

def odd_ones_out(x):
	d = dict()

	for val in x:
		if val in d:
			d[val] += 1
		else:
			d[val] = 1
	newX = []
	for val in x:
		if d[val]%2 == 0:
			newX.append(val)
	return newX