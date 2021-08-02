input = [1, 2, 3, 4, 5, 6, 8, 9, 10]

def findMissingNum(input):
	n = len(input) + 1
	total_sum = n * (n + 1) / 2
	array_sum = sum(input)
	return total_sum - array_sum

print(findMissingNum(input))
