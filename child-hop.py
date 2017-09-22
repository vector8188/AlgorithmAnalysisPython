#page 109
memo = {0:1}
def hop(num):
	if num < 0:
		return 0 
	elif num == 0:
		return 1
	else:
		memo[num]=hop(num-1)+ hop(num-2) + hop(num-3)
		return memo[num]
print (hop(40))