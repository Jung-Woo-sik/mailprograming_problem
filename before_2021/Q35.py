#Given an array consisting of 0, 1 and 2s, sort this array.

def sort(a):
	low = 0
	high = len(a) - 1
	i = 0
	while i <= high:
		if a[i] == 0:
			a[low], a[i] = a[i],a[low]
			low = low + 1
			i = i + 1
		elif a[i] == 1:
			i = i + 1
		else:
			a[i],a[high] = a[high],a[i]
			high = high -1
	return a

print(sort([0, 1, 2, 2, 0, 0, 0, 1]))
