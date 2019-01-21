#Given an integer array and an integer K, check if sum of 3 elements from the array equals to K.
def solution(arr, k):
	for x in range(len(arr)):
		for y in range(x + 1, len(arr)):
			for z in range(y + 1, len(arr)):
				if arr[x] + arr[y] + arr[z] == k:
					return True
	return False

