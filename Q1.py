#Given an integer array, find the largest consecutive sum of elements.

def sol(arr):
	maxSum = arr[0]
	currentSum = arr[0]
	for i in range(1,len(arr)):
		currentSum = max(currentSum+arr[i],arr[i])
		maxSum = max(currentSum,maxSum)

	return maxSum
