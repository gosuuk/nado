package chap_04._Quiz;

public class java_ {
    public static void main(String[] args) {
        int hour = 5; // 주차 시간
        boolean isSmallcar = false; // 경차 여부
        boolean with = false;// 장애인 차량 여부
        
        int fee = hour * 4000; // 주차 정산 요금 시간당 4000원 곱하기
        
        // 30000 원 초과 시 일일 최대 요금으로 수정
        if (fee > 30000) {
            fee = 30000; // 일일 최대 요금 적용
        }
        
        // 경차 또는 장애인 차량인 경우 50% 할인
        if (isSmallcar || with) {
            fee /= 2;
        }

        // 실행 결과 출력
        System.out.println("주차 요금은" + fee + "원입니다.");
    }
}
