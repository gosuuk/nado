package chap_06;

public class _04_parameterAndReturn {

    public static int getPower(int number) {
        int result = number * number;
        return result;
    }
    public static void main(String[] args) {
        int reval = getPower(2);
        System.out.println(reval); // 2 * 2 =4

        reval = getPower(3);
        System.out.println(reval);

        System.out.println(getPower(2));
    }
}
