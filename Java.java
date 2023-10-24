import java.util.Scanner;

public class Java {

    public static double get_coef(int index) {
        Scanner input = new Scanner(System.in);
        String coef_1 = input.nextLine();
        int flag = 1;
        double coef = 0;

        while(flag == 1) {
            try {
                coef = Double.parseDouble(coef_1);
                flag = 0;
            }
            catch(NumberFormatException e) {
                System.out.println("Коэффициент " + index + " введен некорректно! Введите его снова.");
                coef_1 = input.nextLine();
            }
        }
        return coef;
    }

    public static double[] solve(double a, double b, double c) {
        double[] roots = new double[4];
        double dis = b*b - 4*a*c;

        if (dis >= 0.0) {
            double x1_1 = (-b + Math.sqrt(dis))/(2*a);
            int flag1 = 1;
            int flag2 = 1;

            if (x1_1 >= 0) {
                double x1 = Math.sqrt(x1_1);
                double x2 = x1 * (-1);
                flag1 = 0;
                roots[0] = x1;
                roots[1] = x2;
            }

            double x3_3 = (-b - Math.sqrt(dis))/(2*a);
            if (x3_3 >= 0) {
                double x3 = Math.sqrt(x3_3);
                double x4 = x3 * (-1);
                flag2 = 0;
                roots[2] = x3;
                roots[3] = x4;
            }

            if (flag1 == 0 && flag2 == 0) return roots;
            else if (flag1 == 0) {
                double[] roots1 = {roots[0], roots[1]};
                return roots1;
            }
            else if (flag2 == 0) {
                double[] roots2 = {roots[2], roots[3]};
                return roots2;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        double a = get_coef(1);
        double b = get_coef(2);
        double c = get_coef(3);

        double[] roots = solve(a, b, c);

        if (roots != null) {
            System.out.println("Корни уравнения: " + roots[0] + ", " + roots[1]);
            if (roots.length == 4) {
                System.out.println("Корни уравнения: " + roots[2] + ", " + roots[3]);
            }
        }
        else System.out.println("Нет действительных корней уравнения.");
    }
}
