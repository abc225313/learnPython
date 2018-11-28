while(True):
	try:
		number=int(input('輸入數字\n'))
		if number is not None:
			for n in range(2,number):
				if number%n==0:
					print('他不是是質數')
					#可以分解
					break
				
		else:
			print('you have to input somethings')
	except ValueError as err:
		print(err)
		break
