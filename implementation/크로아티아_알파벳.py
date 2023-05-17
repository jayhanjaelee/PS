def solution1():
    """
    i) 크로아티아 알파벳에 대하여 반복문 실행
    ii) 입력받은 문자열에 크로아티아 알파벳이 포함되어 있으면 * 로 치환
    iii) 수정이 완료된 단어의 길이 출력
    iv) 주의: dz= 가 z= 보다 앞의 요소에 위치해 있어야함
        z= 요소에 대하여 먼저 * 로 치환되면 dz= 에 해당하는 크로아티아 알파벳 탐색하는것이 불가능.
    """

    word = input()
    lst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for i in lst:
        word = word.replace(i, "*")
    print(len(word))


def solution2():
    """
    i) 문자열에서 크로아티아 알파벳을 발견하면 cnt += 1
    ii) 발견된 문자열의 범위를 !로 치환
    iii) 수정이 완료된 문자열의 갯수 출력
    """

    result = 0
    cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    word = input()

    for c in cro:
        while True:
            loc = word.find(c)
            if loc == -1:
                break

            result += 1
            word = word[:loc] + "!" + word[loc + len(c) :]
            print(word, c)

    word = word.replace("!", "")
    print(result + len(word))


solution1()
# solution2()
