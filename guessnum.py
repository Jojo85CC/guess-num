import random

r = random.randint(1,100)

while True :
	num = input('請猜數字:')
	num = int(num)
	if num == r :
		print ('終於猜對了')
		break
	elif num > r :
		print('猜錯了比數字大',num-r)
	elif num < r :
		print('猜錯了比數字小',r-num)




		
 
		
