import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Scanner;

class 주사위_세개 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int ans = 0;
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if (a == b && a == c && b == c) {
            ans = 10000 + (a * 1000);
        } else if (a == b || a == c) {
            ans = 1000 + (a * 100);
        } else if (b == c) {
            ans = 1000 + (b * 100);
        } else {
            ans = Math.max(a, Math.max(b, c)) * 100;
        }

        System.out.println(ans);
    }
}