x = [1,4,7,8,10]
y = [2,3,9]
z = len(x)
for i in y:
	x.append(i)
x.sort()
answer1 = x[0:z]
answer2 = x[z:len(y)]

print(answer1)
