import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        /**
         * 계단 아래 시작점부터 꼭대기에 위치한 도착점까지 가는 게임
         * 일정한 점수가 쓰여있는게 그 점수
         *
         * 계단 오르는 규칙
         * 1. 한번에 한계단 또는 두계단씩 오를 수 있음
         * 2. 연속된 세개의 계단을 모두 밟아서는 안됨 (계속 한계단씩 갈 순 없음)
         * 3. 마지막 계단은 반드시 밟아야 함
         *
         * 계단은 300 이하
         * - 인풋
         * 1. 계단의 개수 N 입력 받기
         * 2. N개 리스트 만들기
         * 3. N개만큼 for문을 돌려서 각 계단의 점수를 입력받기
         *
         * - 로직
         * 결국 다 돌아야 할 것으로 예상
         * dp임 -> 메모이제이션이나 타뷸레이션으로 풀어야 함
         * 처음부터 한 계단 간 경우와 두 계단 간 경우로 나눠서 더 나은 큰 수를 채택
         */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int [] score = new int[N];
        for (int i = 0; i < N; i++){
            score[i] = Integer.parseInt(br.readLine());
        }

        if (N == 1) {
            System.out.println(score[0]);
            return;
        }

        if (N == 2) {
            System.out.println(score[0] + score[1]);
            return;
        }


        int [] dp = new int[N];
        dp[0] = score[0];
        dp[1] = dp[0]+score[1];
        dp[2] = Math.max(dp[0]+score[2], score[1]+score[2]);

        for (int i = 3; i < N; i++){
            dp[i] = Math.max(dp[i-2]+score[i], dp[i-3]+ score[i-1]+score[i]);
        }
        System.out.println(dp[N-1]);

    }
}