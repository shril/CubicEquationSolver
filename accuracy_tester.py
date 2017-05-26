import CubicEquationSolver
from random import randint
import numpy as np
import timeit



no_of_iterations = 100000

store = []

for i in range(no_of_iterations):
	#a = randint(-10000, 10000)
	b = randint(-10000, 10000)
	c = randint(-10000, 10000)
	d = randint(-10000, 10000)
	a = 0
	store.append([a, b, c, d])

start = timeit.default_timer()

for i in range(no_of_iterations):
	old_root = np.roots([store[i][0], store[i][1], store[i][2], store[i][3]])
	fast_root = CubicEquationSolver.solve(store[i][0], store[i][1], store[i][2], store[i][3])
	ct = 0
	for r1 in old_root:
                for r2 in fast_root:
                        if str(r1.real) == str(r2.real) and str(r1.imag) == str(r2.imag): ct+=1

        #if ct == 3: print "Correct!"
        if ct > 2: print "Anomaly! roots are ->\nOld root -> ",old_root,"\nnew_root -> ",new_root
        elif ct < 2: print "Might be wrong !\nOld root -> ",old_root,"\nnew_root -> ",fast_root
                

