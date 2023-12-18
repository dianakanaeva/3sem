from behave import given, when, then
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from EquationSolver import EquationSolver


@given('I have an equation solver with coefficients {a:d}, {b:d}, {c:d}')
def step_given_equation_solver(context, a, b, c):
    context.solver = EquationSolver(a, b, c)

@when('I solve the equation')
def step_when_solve_equation(context):
    context.result = context.solver.solve()

@then('I expect the result to be {expected_result}')
def step_then_check_result(context, expected_result):
    if expected_result == 'None':
        expected_result = None
    else:
        expected_result = tuple(float(x) for x in expected_result.split('and'))

    assert context.result == expected_result