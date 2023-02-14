package chap_04;

public class _04_switchCase {
    public static void main(String[] args) {
        // switch case
        // 석차에 따른 장학금 지급
        // 1등 : 전액 장학금
        // 2등 : 반액 장학금
        // 3등 : 반액 장학금
        // 그외 : 장학금 대상 아님
        
        int ranking = 1; // 1등
        if (ranking == 1) {
            System.out.println("전액장학금");
        } else  if (ranking == 2 || ranking ==3) {
            System.out.println("반액장학금");
        } else {
            System.out.println("장학금 대상 아님");
        }

        // switch Case 문을 이용
        ranking = 2;
        switch (ranking) {
            case 1:
                System.out.println("전액 장학금");
                break;
            case 2:
                System.out.println("반액 장학금");
                break;
            case 3:
                break;
        }
        System.out.println("등급 제품의 가격 : " +"원");

        int score = 95;
        if (score >= 90)
            System.out.println("A");
        else if (score>= 80)
            System.out.println("B");
    }
}
