import random
start = input('請決定隨機數字範圍開始值')
end = input('請決定隨機數字範圍結束值')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True :
	count += 1
	num = input('請猜數字:')
	num = int(num)
	if num == r :
		print ('終於在第',count,'猜對了')
		break
	elif num > r :
		print('猜錯了比數字大',num-r)
	elif num < r :
		print('猜錯了比數字小',r-num)
	print('你已經猜',count,'次')





		
 
		
