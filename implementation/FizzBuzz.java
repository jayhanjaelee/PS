import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class FizzBuzz {
  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int x = Integer.parseInt(st.nextToken());
    int y = Integer.parseInt(st.nextToken());
    int n = Integer.parseInt(st.nextToken());

    for (int i = 1; i <= n; i++) {
      if (i % x == 0) {
        if (i % y == 0) {
          System.out.println("FizzBuzz");
        } else {
          System.out.println("Fizz");
        }
      } else if (i % y == 0) {
        System.out.println("Buzz");
      } else {
        System.out.println(i);
      }
    }
  }

  public static void main(String[] args) throws Exception {
    new FizzBuzz().solution();
  }
}