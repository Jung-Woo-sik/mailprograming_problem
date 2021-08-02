#Implement an O(n log n) time complexity sorting algorithm.

def quicksort(data, start, end):
	if start < end:
		pivot = start;
		for i in range(start,end):
			if data[i] < data[end]:
				swap(data,i,pivot)
				pivot = pivot +1
		swap(data,pivot,end);
		quicksort(data,start,pivot-1)
		quicksort(data,pivot+1,end)

def swap(data,a,b):
	temp = data[a]
	data[a] = data[b]
	data[b] = temp


if __name__ == "__main__":
	a = [3,1,5,6]
	print (quicksort(a,0,len(a)-1))
