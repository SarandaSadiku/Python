def average():
	a=[1,2,5,10,255,3]
	sum=0
	avg=0
	for element in a:
		sum+=element
		avg=sum/len(a)
	print avg

average()