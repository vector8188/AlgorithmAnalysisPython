
def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False
	while not found and first <= last:
		# manipulate mid point here as this is the place
		# which brings it closer to the solution
		mid = (first + last) // 2
		if alist[mid] == item:
			found = True
		else:
			if alist[mid] > item:
				# this means the searched 'item' is on the left hand side
				last = mid - 1
			else:
				first = mid + 1
	return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,100]
print(binarySearch(testlist, 100))


print(binarySearch(testlist, 19))
