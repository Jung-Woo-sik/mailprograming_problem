#Given a sorted integer array and an integer N, check if N exists in the array.

def binarySearch( in_arr, n):
	start = 0;
	end = len(in_arr) -1
	
	while end >= start :
		middle = (start+end) //2
		if in_arr[middle] == n:
			return True
		if in_arr[middle] < n:
			start = middle +1
		if in_arr[middle] > n:
			end = middle -1;
	return False;


if __name__ == "__main__":
	a = [1,4,5,6,7,9]
	print (binarySearch(a,10))
