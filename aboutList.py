grade_list = [("小雞", 100), ("兩大類", 0), ("小喵", 80), ("小蟲", 60)]
#del grade_list[0]
#grade_list.append(tuple(('小雞',100)))
for n in range(len(grade_list)):#0123
	for i2 in range(len(grade_list)-1):
		if(grade_list[i2][1]>grade_list[i2+1][1]):
			x=grade_list[i2+1]
			y=grade_list[i2]
			grade_list.remove(x)
			grade_list.insert(i2,x)
			grade_list.remove(y)
			grade_list.insert(i2+1,y)
			print(grade_list)
