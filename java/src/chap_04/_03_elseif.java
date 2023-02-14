package chap_04;

public class _03_elseif {
    public static void main(String[] args) {
        // 조건문 Elseif
        // 한라봉 에이드가 있으면 +1
        // 망고 주스가 있으면 +1
        // 아이스 아메리카노 +1
        boolean hallabongade = false;
        boolean mangojuice = false;
        boolean orangejuice = true;

        if (hallabongade) {
            System.out.println("한라봉 에이드 +1");
        } else if (mangojuice) {
            System.out.println("망고 쥬스 +1");
        } else  if (orangejuice) {
            System.out.println("오렌지 주스 +1");
        }
        else {
            System.out.println("아이스 아메리카노 +1");
        }
        System.out.println("커피 주문 완료#1");
    }
}
