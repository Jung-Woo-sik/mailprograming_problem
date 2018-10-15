
#Given an integer, count number of 1s in binary representation of an integer.
def countSetBits(n):
	count = 0
	while (n):
		n &= (n-1) 
		count+=1
	return count


if __name__ == "__main__":
	print(countSetBits(6))
