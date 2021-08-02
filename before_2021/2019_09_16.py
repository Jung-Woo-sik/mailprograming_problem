x = [0, 2, 0, 3, 0, 5, 6, 0, 0]
y = [1, 8, 9, 10, 15]
z = len(y)
for i in y:
	x.append(i)
x.sort()
print(x[z:])
