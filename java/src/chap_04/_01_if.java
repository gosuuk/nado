package chap_04;

public class _01_if {
    public static void main(String[] args) {
        // 조건문 if
        int hour = 13; // 오전 10시

        // if 문 내에서 하나의 문장을 실행할 때는 {} 생략가능
        if (hour < 14)
            System.out.println("아이스 아메리카노 +1");

        // if 문 내에서 2개 이상의 문장을 실행할 떄는 {} 생갹 불가
        if (hour < 14) {
            System.out.println("아이스 아메맄카노 +1");
            System.out.println("샷추가");
        }
        System.out.println("커피 주문 완료");

        // 오후 2시 이전, 모닝 커피를 마시지 않을 경우?
        hour = 10;
        boolean morningCoffee = false; // 모닝커피
        if (hour < 14 && morningCoffee == false) {
            System.out.println("아이스 아메리카노 +1");
        }
        System.out.println("커피 주문 완료");

        // 오후 2시 이후이거나 모닝 커피를 마신 경우?
        hour = 17;
        morningCoffee = true;
        // if (hour >= 14 || morningCoffee == true) {
        if (hour >= 14 || morningCoffee) {
            System.out.println("아이스 디카페인 커피 +1");
        }
        System.out.println("커피 주문 완료 #3");
    }
}
