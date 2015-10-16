import random

alfa=0.5
beta=0.5
delta=0
psi=0
eta=0.5

u=0.2
v=0.2

for i in range(10000000000):
	r=random.random()
	if r<=0.5:
		u1=alfa*u+delta*v
		v1=beta*u+eta*v
	else:
		u1=alfa+u*(1-alfa)+psi*v
		v1=beta-beta*u+eta*v
	print '%10.4f' %u,'%10.4f' %v	   
	u=u1
	v=v1
	
