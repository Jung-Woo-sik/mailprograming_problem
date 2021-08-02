#Given an integer K, print all binary strings of length K without consecutive 1s.

def printStrings(n, out, last_digit):
	if n == 0 :
		print (out)
		return
	printStrings(n-1, out+"0",0);

	if last_digit ==0:
		printStrings(n-1,out+"1", 1)
	
n = 5;
printStrings(n,"",0)
