#Given an array of strings, find the longest common prefix of all strings.

def longestPrefixLength(arr):
	if len(arr) == 0:
		return 0

	max_prefix = arr[0]
	for i in range(0,len(max_prefix)):
		c = max_prefix[i]
		for j in range(1,len(arr)):
			if i == len(arr[j]) or arr[j][i] != c:
				return i

	return len(max_prefix)

if __name__ == "__main__":
	a = ["apple","apps","ape"]
	print (longestPrefixLength(a))
