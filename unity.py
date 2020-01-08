'''UTF-8 hex helper'''


x = list(map(str, input("Enter a multiple value: ").split())) 
b = len(x)
#print (b)

for i in range(0,b):
	print("%"+x[i], end = "")