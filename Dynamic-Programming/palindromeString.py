def palStr(data):
	length = len(data)
	if length == 1 or length == 0:
		return True

	if data[0] == data[length-1]:
		return palStr(data[1:length-1])

	return False

print(palStr('racecar'))