from collections import defaultdict
import heapq

def rearrange(string):
	frequencies = defaultdict(int)
	for letter in string:
		frequencies[letter] += 1

	heap = []
	for char, count in frequencies.items():
		heapq.heappush(heap, (-count, char))

	count, char = heapq.heappop(heap)
	result = [char]

	while heap:
		last = (count + 1, char)
		count, char = heapq.heappop(heap)
		result.append(char)

		if last[0] < 0:
			heapq.heappush(heap, last)

	if len(result) == len(string):
		return "".join(result)
	else:
		return ""

if __name__ == "__main__":
	print (rearrange("aaabbc"))
