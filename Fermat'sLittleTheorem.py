# if a belongs to Z then a^p = a mod p

def fermat(a,p):
	return (a**p)%p

a_arr =[2 ,3,4,5,6,7,8,11,12,13]
p_arr =[2,3,5,7,11]

for a in a_arr:
	for p in p_arr:
		print(f'a={a}, p={p}:  {fermat(a,p)} ')



#note : little theorem only work when p > a 