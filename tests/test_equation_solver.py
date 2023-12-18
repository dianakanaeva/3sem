import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import EquationSolver

def test_zero_discr():
    solver = EquationSolver.EquationSolver(1, -2, 1)
    result = solver.solve()
    assert result == (1.0, -1.0, 1.0, -1.0)

def test_negative_discr():
    solver = EquationSolver.EquationSolver(1, 1, 1)
    result = solver.solve()
    assert result == None