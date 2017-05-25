# Cubic Equation Solver

Useful Information about the script :

* Used as a subsitute of np.roots() function which utilizes Eigen Value Matrix Method for finding roots of the polynomial.

* ~6x faster than np.roots but exclusive to cubic polynomials.

* Manages the issue of inherent in the power basis representation of the polynomial in floating point numbers.

* Time Complexity of snippet is O(1).

[Algorithm Link](http://www.1728.org/cubic2.htm)

### Sample Code
```python
import CubicEquationSolver
CubicEquationSolver.solve(1, 0, 1, 0)
```
```
Output: [ 0.+0.j  0.+1.j -0.-1.j]
```
