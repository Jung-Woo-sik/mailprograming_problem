def solution( input_arr):
	startIndex = 0
	index = startIndex
	for i in input_arr:
		if i != 0 and index == startIndex:
			return False
		index = input_arr[index]
	if index == startIndex:
		return True
	return False


