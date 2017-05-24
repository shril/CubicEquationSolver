import CubicEquationSolver
from random import randint
import numpy as np



for i in xrange(1000):
	a = randint(-10000, 10000)
	b = randint(-10000, 10000)
	c = randint(-10000, 10000)
	d  =randint(-10000, 10000)

	roots_fast = CubicEquationSolver.solve(a, b, c, d)
	roots_slow = np.roots([a, b, c, d])

	print "coeff-> ", a, " ", b, " ", c, " ", d
	print roots_fast
	print roots_slow
	print "--------------------------------------\n\n"
	'''
	match = False
	ct = 0
	for i in range(3):
		for j in range(3):
			if roots_fast[i] == roots_slow[j]: ct += 1

	if ct >= 3: print "correct"
	else: print "wrong!" 
	'''