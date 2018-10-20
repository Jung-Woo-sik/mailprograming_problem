#

def search(arr,start,end,k):
	if start > end:
		return -1

	mid = (start+end)//2;

	if arr[mid] ==k :
		return mid
	
	if arr[start] <= arr[mid]:
		if k >= arr[start] and k <= arr[mid]:
			return search(arr,start,mid-1,k)
		return search(arr,mid+1,end,k)

	if k >= arr[mid] and k <= arr[end]:
		return search(arr,mid+1,end,k)

	return search(arr,start,mid-1,k)
	
if __name__ == "__main__":
	a = [2,4,5,1]
	print(search(a,0,len(a)-1,3))
