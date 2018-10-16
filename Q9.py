#Given a file path containing "./" and "../", convert the path to a unix standard file path that does not contain "./" and "../".


def standardize(path):
	stack = []
	path = path.split("/")

	for segment in path:
		if segment == ".":
			continue 
		elif segment == "..":
			if len(stack) > 1:
				stack.pop()
		else:
			stack.append(segment)

	return "/".join(stack)

if __name__ == "__main__":
	print(standardize("/usr/bin/o0o0/sik/../"))

