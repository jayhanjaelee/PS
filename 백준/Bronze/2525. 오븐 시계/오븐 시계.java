import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int curHour = Integer.parseInt(st.nextToken());
        int curMin = Integer.parseInt(st.nextToken());
        int curTotalMin = curHour * 60 + curMin;

        int requiredMin = Integer.parseInt(br.readLine());

        int resultMin = curTotalMin + requiredMin;

        int estimatedHour = (resultMin / 60) % 24;
        int estimatedMin = resultMin % 60;
        System.out.printf("%d %d%n", estimatedHour, estimatedMin);

        br.close();
    }
}