def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	mid = len(lst)//2
	left = merge_sort(lst[:mid])
	right = merge_sort(lst[mid:])
	return merge(left,right)

def merge(left,right):
	if not left:
		return right
	if not right:
		return left	

	if left[0] < right[0]:
		return [left[0]] + merge(left[1:],right)
	return [right[0]] + merge(left, right[1:])

lst = [4, 5, 1, 6, 3]
print(merge_sort(lst))