import numpy as np
# import matplotlib.pyplot as plt
import random 

r = 2
ntotal = 10000
nsample = 10
nhits_list = []
phi_list = []

for i in range(nsample):
	nhits = 0
	for j in range(ntotal):
		rand_ = np.random.rand()
		xrand = -r + (rand_ * (2*r))
		rand_ = np.random.rand()
		yrand = -r + (rand_ *(2*r))
		rrand = np.sqrt(xrand**2 + yrand**2)
		if rrand <= r:
			nhits += 1
	nhits_list.append(nhits);		
	phi = 4 * (nhits/ntotal)
	phi_list.append(phi)

print(phi_list)
print(np.mean(phi_list))

# plt.plot(r,)