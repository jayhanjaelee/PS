import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class 알람_시계 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        m = m - 45;
        if (m < 0) {
            h = h - 1;
            m = 60 - (int) Math.abs(m);
        }

        if (h < 0) {
            h = 24 - (int) Math.abs(h);
        }

        System.out.printf("%d %d%n", h, m);
    }
}