package chap_06;

import javax.imageio.stream.ImageInputStream;

public class _05_Over {
    public static int getPower(int number) {
        int result = number * number;
        return result;

    }
    public  static int getPowerStr(String strNumber) {
        int number = Integer.parseInt(strNumber);
        return number * number;
    }
    public static int getPowerByExp(int number, int exponent) {
        int result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= number;
        }
        return result;

    }
    public static void main(String[] args) {
        System.out.println(getPower(3)); //3 * 3 = 9
        System.out.println(getPowerStr("4")); //4 * 4 = 16
        System.out.println(getPowerByExp(3, 3));
    }
}
