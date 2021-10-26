def reverseString(data):
	if data == '':
		return ''
	return reverseString(data[1:])+data[0]

print(reverseString('abcd'))