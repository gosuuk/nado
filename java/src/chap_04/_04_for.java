package chap_04;

public class _04_for {
    public static void main(String[] args) {
        // 반복문 for
        // 니코 매장
        System.out.println("어서오세요 니코입니다.");

        // 반복문 사용 for
        for (int i = 0; i < 10; i++) {
            System.out.println("어서오세요 니코입니다. " + i);
        }
        
        // 짝수만 출력
        for (int i = 0; i <10; i +=2) {
            System.out.print(i);
            
        }
        System.out.println();
        for (int i = 1; i < 10; i += 2) {
            System.out.print(i);

        }
        System.out.println();
        // 거꾸로 숫자
        // 5, 4, 3, 2, 1
        for (int i = 5; i > 0; i-= 1) {
            System.out.print(i);
        }

        System.out.println();

        int sum = 0;
        for (int i = 1; i < 11; i++) {
            sum += i;
            System.out.println("현재까지 총합은" + sum + "입니다");

        }
        System.out.println("1부터 10까지의 모든 수의 총합은" + sum + "입니다");
    }
}
