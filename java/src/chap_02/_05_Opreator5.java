package chap_02;

public class _05_Opreator5 {
    public static void main(String[] args) {
        // 삼항 연산자
        int x = 3;
        int y = 15;
        int max = (x > y) ? x : y;
        System.out.println(max); // 5

        int min = (x < y) ? x : y;
        System.out.println(min); // 3

        x = 3;
        y = 3;
        boolean b = (x == y) ? true : false;
        System.out.println(b);

        String s = (x != y) ? "달라요" : "같아요";
        System.out.println(s);
    }
}