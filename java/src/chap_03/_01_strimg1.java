package chap_03;

public class _01_strimg1 {
    public static void main(String[] args) {
        String s = "I like java and python and c.";
        System.out.println(s);

        // 문자열의 길이
        System.out.println(s.length()); // 29

        // 대소문자 변환
        System.out.println(s.toUpperCase()); // 대문자로
        System.out.println(s.toLowerCase()); // 소문자로

        // 포함 관계
        System.out.println(s.contains("java")); // 포함되면 true
        System.out.println(s.contains("c#")); // 포함 안되면 false
        System.out.println(s.indexOf("java")); // 위치 정보
        System.out.println(s.indexOf("c#")); // 포함되지 않는다면 -1
        System.out.println(s.indexOf("and"));  // 처음 일치하는 위치 정보
        System.out.println(s.lastIndexOf("and")); // 마지막으로 일치하는 위치 정보
        System.out.println(s.startsWith("I like")); // 이 문자열로 시작하면 true (아니면 false)
        System.out.println(s.endsWith(".")); // 이 문자열로 끝나면 true (아니면 false)
    }
}
