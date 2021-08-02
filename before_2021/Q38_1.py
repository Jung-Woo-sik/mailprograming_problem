#Given an integer array, print all non unique elements.

def printDuplicates(arr): 
	dict = {} 
	for element in arr: 
		try: 
			dict[element] += 1
		except: 
			dict[element] = 1

	for item in dict: 
		if(dict[item] > 1): 
			print(item)

