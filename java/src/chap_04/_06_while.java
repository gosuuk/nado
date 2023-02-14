package chap_04;

public class _06_while {
    public static void main(String[] args) {
        // 반복문 while
        int dist = 25; // 전체 거리 25m
        int move = 0; // 현재 이동 거리 0m
        while (move < dist) {
            System.out.println("발차기를 계속 합니다");
            System.out.println("현재 이동 거리 : " + move);
            move += 3; // 3미터 이동
        }
        System.out.println("도착했습니다.");

        // 무한 루프
    }
}
