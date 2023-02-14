package chap_05;

public class _Quiz_05 {
    public static void main(String[] args) {
        int[] sizeArray = new int[10];
        for (int i = 0; i < sizeArray.length; i++) {
            sizeArray[i] = 250 + (5 * i);
        }
        for (int size:
                sizeArray) {
            System.out.println("사이즈 " + size + " (재고 있음)");
        }


        System.out.println("-------------------------");
        // 세로 크기 10 x 가로크기 15에 해당하는 영화관 좌석
        String[][] seats3 = new String[10][1];
        String[] eng = {"250","255","260","265","270","275","280","285","290","295"};
        for (int i = 0; i < seats3.length; i++) {
            for (int j = 0; j < seats3[i].length; j++) {
                seats3[i][j] = eng[i];
            }

        }
        // 영화관 좌석 확인
        for (int i = 0; i < seats3.length; i++) {
            for (int j = 0; j < seats3[i].length; j++) {
                System.out.print(seats3[i][j] + " ");
            }
            System.out.println("사이즈 (재고 있음)");
        }
    }
}
