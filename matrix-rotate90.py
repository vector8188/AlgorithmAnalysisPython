matrix = [['X00','X01','X02'],['X10','X11','X12'],['X20','X21','X22']]
agg = []

for j in range(0, len(matrix)):
	mat = []
	for i in matrix:
		mat = mat + [i[j]]
	agg.append(mat)
	
print (matrix)
print(agg)