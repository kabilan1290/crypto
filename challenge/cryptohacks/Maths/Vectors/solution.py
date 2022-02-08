v = [2,6,3]
w = [1,0,0]
u = [7,7,2]


v_2 = [i*2 for i in v]
u_2 = [i*2 for i in u]

v_w =[]
for i in range(0,3):
	res = v_2[i] - w[i]
	v_w.append(res)

v_w_3 = [i*3 for i in v_w]
res1 =0
for i in range(0,3):
	res1 += v_w_3[i] * u_2[i]
print(res1)


