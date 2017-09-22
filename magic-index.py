def magic_index(array, start, end):
	if (end > start or start < 0 or end > len(array)):
		return False
	mid = (start + end)//2
	if array[mid] == mid:
		return mid
	elif array[mid] > mid:
		magic_index(array, start, mid-1)
	else:
		magic_index(array, mid+1, end)
		