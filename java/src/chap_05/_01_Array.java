package chap_05;

public class _01_Array {
    public static void main(String[] args) {
        // 배열 : 같은  자료형의 값 여러 개를 저장하는 연속된 공간
        String coffeeRoss = "아메리카노";
        String coffeeRachel = "카페모카";
        String coffeeChandler = "라떼";
        String coffeeMonica = "카푸치노";

        System.out.println(coffeeRoss + "하나");
        System.out.println(coffeeRachel + "하나");
        System.out.println(coffeeChandler + "하나");
        System.out.println(coffeeMonica + "하나");
        System.out.println("주세요");


        // 배열 선언 첫 번째 방법
//        String[] coffes = new String[4];
//
//        // 두 번째 방법
//        // String coffes[] = new String[4];
//        coffes[0] = "아메리카노"; // 0 부터 시작
//        coffes[1] = "카페 모카";
//        coffes[2] = "라떼";
//        coffes[3] = "카푸치노";
//
        // 세 번째 방법
        String[] coffes = new String[] {"아메리카노"};

        // 네 번째 방법
        String[] coffeees = {"아메리카노", "카페모카"};

        System.out.println("--------------------------");

        // 커피 주문
        System.out.println(coffes[0] + "하나"); //아메리카노 하나
        System.out.println(coffes[1] + "하나"); // 카페모카 하나
        coffeees[2] = "에스프레소";
        System.out.println(coffes[2] + "하나");
        System.out.println(coffes[3] + "하나");
        System.out.println("주세요");

    }
}
