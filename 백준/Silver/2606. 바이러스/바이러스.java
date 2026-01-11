
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    static boolean[] visited;
    static int count = 0;
    static ArrayList<Integer>[] graph;

    public static void main (String[] args ) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 컴퓨터 수
        int n = Integer.parseInt(br.readLine());
        // 연결된 쌍의 수
        int m = Integer.parseInt(br.readLine());

        visited = new boolean[n+1];
        // ArrayList 인접 리스트 만들기
        graph = new ArrayList[n+1];
        for (int i=1; i <= n; i++){
            graph[i] = new ArrayList<>();
        }

        // 인접 리스트 정보 입력
        for (int i = 0; i < m; i++ ){
            // 공백으로 분리하여 인풋 받기
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);

            graph[a].add(b);
            graph[b].add(a);
        }

        dfs(1);
        System.out.println(count);
        
    }

    static void dfs(int node){
        visited[node] = true;

        for (int next : graph[node]){
            if (!visited[next]){
                count++;
                dfs(next);
            }
        }
    }
}
