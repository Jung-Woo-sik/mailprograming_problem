#Given a sorted array, print all elements where its value is equal to the index.

def fixed_point(array):
	low, high = 0, len(array)

	while low <= high:
		mid = (low + high) // 2if array[mid] == mid:
			print mid
			returnelif array[mid] < mid:
			low = mid + 1else:
			high = mid - 1

	print "not found"
