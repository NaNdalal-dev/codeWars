#Link:
#https://www.codewars.com/kata/585a033e3a36cdc50a00011c/train/python

def freq_seq(s, sep):
    d = dict()
    #Counting Frequeny of each character
    for val in s:
    	if val in d:
    		d[val] += 1
    	else:
    		d[val] = 1


    new_s = ''
    for val in s:
    	new_s += str(d[val])
    return f'{sep}'.join(new_s)
