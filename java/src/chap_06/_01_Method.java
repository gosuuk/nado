package chap_06;

public class _01_Method {
    // 메소드 정의
    public static void sayhello() {
        System.out.println("안녕하세요?");
    }
    public static void main(String[] args) {
        // 메소드 호출
        System.out.println("메소드 호출 전");
        sayhello();
        sayhello();
        sayhello();
        System.out.println("메소드 호출 후");
    }
}
