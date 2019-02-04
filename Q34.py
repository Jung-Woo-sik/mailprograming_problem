#Given a string, print all permutations of characters in the string.

def solve( string, l,r):
	if l ==r :
		print(string)
	else :
		for i < r :
			string = swap(string,l,i)
			solve(string,l+1,r)
			string = swap(string,l,i)


def swap(string,i,j):
	sb = string

