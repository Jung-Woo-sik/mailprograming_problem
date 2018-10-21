#Given an array and an integer K, shift all elements in the array K times.

def rotate(arr, k):
	n = len(arr)
	k = k % n
	reverse(arr,0,k-1)
	reverse(arr,k,n-1)
	reverse(arr,0,n-1)

def reverse(nums,start,end):
	while start < end:
		temp = nums[start]
		nums[start] = nums[end]
		nums[end] = temp
		start = start + 1
		end = end -1


if __name__ == "__main__":
	a = [1,2,3,4,5]
	k = 2
	rotate(a,k)
	print(a)
