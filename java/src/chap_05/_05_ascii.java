package chap_05;

public class _05_ascii {
    public static void main(String[] args) {
        // 아스키 코드
        char c = 'A'; // 알파벳 대문자는 65부터 시작, 소문자는 97부터 시작 숫자는 48부터 시작
        System.out.println((int)c);
        System.out.println(c);

        c = 'B';
        System.out.println((int)c);
        System.out.println(c);

        c++;
        System.out.println((int)c);
        System.out.println(c);

    }
}
