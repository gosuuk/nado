package chap_02;

public class _Quiz_02 {
    public static void main(String[] args) {
        int sht = 115;
        int log = 121;
        int x = (120 < log) ? sht : log;
        int y = (120 < sht) ? sht : log;
        System.out.println(x);
        System.out.println(y);
        System.out.println("키가" + x+"cm 이므로 탑승 불가능합니다");
        System.out.println("키가" + y+"cm 이므로 탑승 가능합니다.");
    }
}
