#Given an integer array and integer N, find the Nth largest element in the array.

def quickselect(arr,k):
	return quickselection(arr,0,len(arr)-1,k-1)

def quickselection(arr,first,last,k):
	if first <= last:
		pivot = partition(arr,first,last)
		if pivot == k:
			return arr[k]
		if pivot > k:
			return quickselection(arr,first,pivot-1,k)
		return quickselection(arr,pivot+1,last,k)

	return 0

def parttion(arr,first,last):
	pivot_spot = first
	for i in range(first,last):
		if arr[i] > arr[last]:
			swap(arr,i,pivot_spot)
			pivot_spot++;

	swap(arr,pivot_spot,last)
	return pivot_spot

def swap(arr, x, y):
	tmp = arr[x]
	arr[x] = arr[y]
	arr[y] = tmp


