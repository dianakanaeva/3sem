import sys
import math

def get_coef(index):
    coef_1 = sys.argv[index]
    flag = 1
    while(flag):
        try:
            coef = float(coef_1)
            flag = 0
        except:
            print("Коэффициент ", index, " введен некорректно! Введите его снова.")
            coef_1 = input()
    return coef

def solve(a, b, c):
    dis = b**2 - 4*a*c
    if dis >= 0.0:
        x1_1 = (-b + math.sqrt(dis))/(2*a)
        flag1 = 0
        flag2 = 0

        if x1_1 >= 0:
            x1 = math.sqrt(x1_1)
            x2 = x1 * (-1)
            flag1 = 1

        x3_3 = (-b - math.sqrt(dis))/(2*a)
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

    return 0

def main():
    a = get_coef(1)
    b = get_coef(2)
    c = get_coef(3)

    roots = solve(a, b, c)

    if roots:
        print("Корни уравнения:", roots)
    else:
        print("Нет действительных корней уравнения.")

if __name__ == "__main__":
    main()
