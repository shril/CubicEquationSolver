import CubicEquationSolver
from random import randint
import numpy as np
import timeit



no_of_iterations = 2000000

store = []

for i in range(no_of_iterations):
	a = randint(-10000, 10000)
	b = randint(-10000, 10000)
	c = randint(-10000, 10000)
	d = randint(-10000, 10000)
	store.append([a, b, c, d])

start = timeit.default_timer()

for i in range(no_of_iterations):
	roots_slow = np.roots(store[i])

stop = timeit.default_timer()
print "Old way of finding roots takes time for ", no_of_iterations, " iterations is -> ", stop - start

start = timeit.default_timer()

for i in range(no_of_iterations):
	roots_fast = CubicEquationSolver.solve(store[i][0], store[i][1], store[i][2], store[i][3])

stop = timeit.default_timer()
print "New way of finding roots takes time for ", no_of_iterations, " iterations is -> ", stop - start
