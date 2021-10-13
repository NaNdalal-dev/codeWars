#Link
#https://www.codewars.com/kata/58acfe4ae0201e1708000075/train/python

def invite_more_women(arr):
    women = men = 0
    count = 0
    for gender in arr:
    	count += 1
    	if gender == -1:
    		women += 1
    	else:
    		men += 1
    print(women,men)
    if women == count:
    	return False
    elif men == count:
    	return True
    elif men > women:
    	return True
    elif women > men:
    	return False
    elif men == women:
    	return False
    else:
    	return True
