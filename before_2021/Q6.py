def solution(nums):
	smallest_impossible = 1
	for n in nums:
		if n <= smallest_impossible:
			smallest_impossible += n
		else:
			return smallest_impossible


if __name__ == "__main__":

	arr = [1,2,3,8]
	print(solution(arr))
