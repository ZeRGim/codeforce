import sys
input = sys.stdin.readline
def solving(m1,m2,given): #반복의 핵심이 되는 기본 골자, 3등분에서의 위치를 return해줌
    if m1*m2 == given:
        return 2
    elif m1*(m2+1) == given:
        return 1
    elif (m1+1)*(m2+1) == given:
        return 0
    else:
        return 3

t = int(input())
for _ in range(t):
    m1 = 334 #처음 1/3지점
    m2 = 667 #처음 2/3지점
    min_ = 1 #처음 최솟값
    max_ = 1000 #처음 최댓값
    #m1,m2,min,max값 설정이 모조리 잘 못 되었음. 기존의 333 666 0 999는 범위와 맞지 않을 뿐더러, 함수를 진행했을 때 3등분 과정에서 미세한 오차가 생길 수 밖에 없어, \
        # 5회 진행하였을 때 모두 같은 결과가 나오지 않음 (계산상 모든 테스트케이스에서 5회를 진행하면 min과 max의 차이가 4가 나야함.) 
    for i in range(5):
        # if max_ - min_ <= 5: #차이가 2이하로 좁혀지면 브레이크
        #     break  #필요없는 부분, 왜냐면 어차피 5번진행하기 전까진 이처럼 좁혀지지 않음 .
        print(f"? {m1} {m2}")
        sys.stdout.flush()
        given = int(input().strip())
        solres = solving(m1,m2,given) #위 함수를 적용
        if solres == 0: #정답위치에 맞게 min, max, m1, m2 재정의
            max_ = m1
            temp = (max_-min_)//3 #다시 3등분하기 위한 간격  #기존 m2-m1에서 max-min으로 바꿈, 중간값끼리 계산시 오류가 생길수도 있을 것이라고 생각했기 때문 .
            m2 = m1 - temp
            m1 = min_ + temp
        elif solres == 1:
            min_ = m1
            max_ = m2
            temp = (max_-min_)//3 #다시 3등분하기 위한 간격
            m2 = m2 - temp
            m1 = m1 + temp
        elif solres == 2:
            min_ = m2
            temp = (max_-min_)//3 #다시 3등분하기 위한 간격
            m1 = m2 + temp
            m2 = max_ - temp
    mean = (min_+max_)//2 #이부분도 m1,m2로 계산하지 않고, 최소 최대를 이용해 계산하여, 모든 테스트케이스에서 일정하게 나오도록 조정함 .
    print(f"? {min_} {mean}")
    sys.stdout.flush()
    given = int(input().strip())
    solres = solving(min_,mean,given)
    if solres == 2:
        print(f"? {mean+1} {mean+2}")
        sys.stdout.flush()
        given = int(input().strip())
        solres = solving(mean+1,mean+2,given)
        if solres == 0:
            print(f"! {mean+1}")
        elif solres == 1:
            print(f"! {mean+2}")
        else:
            print(f"! {mean+3}")
    elif solres == 0:
        print(f"! {min_}")
    elif solres == 1:
        print(f"? {mean-1} {mean}")
        sys.stdout.flush()
        given = int(input().strip())
        solres = solving(mean-1,mean,given)
        if solres == 1:
            print(f"! {mean}")
        elif solres == 0:
            print(f"! {mean-1}")