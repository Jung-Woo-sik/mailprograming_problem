# Given an integer array, find the greatest common denominator of all elements.

def gcd(a,b):
	if a == 0 :
		return b

	return gcd(b%a,a)

def getGCD(arr,n):
	result = arr[0]
	for a in arr:
		result = gcd(a,result);
	return result

if __name__ == "__main__":
	a = [2,4,6,8]
	print(getGCD(a,len(a)))
