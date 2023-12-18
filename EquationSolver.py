import math

class EquationSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        dis = self.b**2 - 4*self.a*self.c
        if dis >= 0.0:
            x1_1 = (-self.b + math.sqrt(dis))/(2*self.a)
            flag1 = 0
            flag2 = 0

            if x1_1 >= 0:
                x1 = math.sqrt(x1_1)
                x2 = x1 * (-1)
                flag1 = 1

            x3_3 = (-self.b - math.sqrt(dis))/(2*self.a)
            if x3_3 >= 0:
                x3 = math.sqrt(x3_3)
                x4 = x3 * (-1)
                flag2 = 1

            if flag1 and flag2:
                return x1, x2, x3, x4
            elif flag1:
                return x1, x2
            elif flag2:
                return x3, x4

        return None