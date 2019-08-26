a = [1,2,3,4,2]
b = list(set(a))
for i in b:
	a.remove(i)
print(a)
