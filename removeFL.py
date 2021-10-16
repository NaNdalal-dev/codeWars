#Link:
#https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python

def remove_char(s):
	new_s = ''
	for i in range(1,len(s)-1):
		new_s += s[i]
	return new_s

#OR 
#remove_char = lambda s : s[1:-1]