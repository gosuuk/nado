package chap_02;

public class _01_operator {
    public static void main(String[] args) {
        // 산술 연산자

        // 일반 연산
        System.out.println(4 + 2);
        System.out.println(4 - 2);
        System.out.println(4 * 2);
        System.out.println(4 / 2);
        System.out.println(4 % 2);

        // 변수를 이용한 연산
        int a = 20;
        int b = 10;
        int c;

        c = a + b;
        System.out.println(c);

        // 은행 대기번호 표
        int waiting = 0;
        System.out.println("대기인원 : " + waiting++); //대기인원 0
        System.out.println("대기인원 : " + waiting++); //대기인원 1
        System.out.println("대기인원 : " + waiting++); //대기인원 2
        System.out.println("대기인원 : " + waiting++); //대기인원 3
        System.out.println("대기인원 : " + waiting++); //대기인원 4
        System.out.println("총 대기 인원 : " + waiting); //총 대기 인원 5

        // 증감 연산
    }
}
