#Given an integer array, print all non unique elements.

def printDuplicates(arr):
	arr.sort()
	print (arr)
		last_dup = None
	for i in range(len(arr) - 1):
		if arr[i] == arr[i+1] and arr[i] != last_dup:
			last_dup = arr[i]
			print arr[i]
