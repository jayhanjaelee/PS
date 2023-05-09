# implementaion

* 일반적으로 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운문제를 지칭하여 구현문제로 분류한다.

* 구현 문제 유형의 예시
  * 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
  * 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
  * 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
  * 적절한 라이브러리를 찾아서 사용해야 하는 문제

## 상하좌우

### Solution

1. 지도에 대한 좌표를 행렬로 생각하여 접근하였음.
2. R U L D 에 대한 2차원 공간에서의 방향 벡터를 dx, dy 리스트로 정의함.
3. 입력받은 방향들에 대해서 반복문을 돌아야 하는데 R U L D 에 대한 문자열로는 방향 벡터에 대한 접근을 할 수 없음.
4. 따라서 R U L D 를 키값으로 가지는 dictionary 를 정의하였고 value 는 방향벡터의 대한 인덱스를 저장하였음.
5. 현재 위치는 x, y 이고 방향벡터와 계산하여 1보다 작을 땐 좌표값 변경을 하지 않도록 구현.