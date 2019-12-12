import random
import math
import time

n = 0
t = 500
alpha = 0.95
n_max = 500000
start_time = time.time()
order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
tmp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

f = open("gr17_d.txt","r")
lines = f.readlines()
list = []
for i in lines:
	item = i.strip().split()
	list.append(item)
f.close()

min = 3500
while(n < n_max):
	fx = 0
	for i in range(0,16):
		fx+= int(list[order[i]][order[i+1]])
	fx += int(list[order[0]][order[16]])
	r1 = random.randint(0,16)
	r2 = random.randint(0,16)
	while r1 == r2 :
		r2 = random.randint(0,16)
	order[r1],order[r2] = order[r2],order[r1]
	diff = fx-min
	if diff < 0 :
		min = fx
		tmp = order
	else :
		order = tmp
		p = random.random()
		if p <= math.exp(-diff/t) :
			min = fx
			tmp = order
	t *= alpha
	n += 1
print('total distance = '+str(min))
ctx=''
for i in range(0,16):
	ctx += str(order[i])
	ctx +=' -> '
	if i == 7:
		ctx+='\n'
ctx += str(order[0])
print(ctx)
print('---- running time : %s seconds ----'%(time.time()-start_time))
	