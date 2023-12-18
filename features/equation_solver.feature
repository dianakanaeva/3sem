Feature: Equation Solver

Scenario: Solving equation with zero discriminant
  Given I have an equation solver with coefficients 1, -2, 1
  When I solve the equation
  Then I expect the result to be 1.0 and -1.0 and 1.0 and -1.0

Scenario: Solving equation with negative discriminant
  Given I have an equation solver with coefficients 1, 1, 1
  When I solve the equation
  Then I expect the result to be None