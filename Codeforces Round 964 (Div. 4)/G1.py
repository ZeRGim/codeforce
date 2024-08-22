import sys
input = sys.stdin.readline
def solving(m1,m2,given):
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
    m1 = 333
    m2 = 666
    min_ = 0
    max_ = 999
    while True:
        if m2 - m1 == 0 or m2 - m1 == 1:
            break
        if m2 - m1 == 2 and m1 > 4:
            break
        print(f"? {m1} {m2}")
        sys.stdout.flush()
        given = int(input().strip())
        solres = solving(m1,m2,given)
        temp = (m2-m1)//3
        if solres == 0:
            max_ = m1
            m2 = m1 - temp
            m1 = min_ + temp
        elif solres == 1:
            min_ = m1
            max_ = m2
            m2 = m2 - temp
            m1 = m1 + temp
        elif solres == 2:
            min_ = m2
            m1 = m2 + temp
            m2 = max_ - temp
    print(f"? {m1} {m2}")
    sys.stdout.flush()
    given = int(input().strip())
    solres = solving(m1,m2,given)
    if solres == 1:
        print(f"! {m2}")
    elif solres == 2  or solres == 0:
        print(f"! {m1}")
    elif solres == 3:
        print(f"? {m1} {m1}")
        sys.stdout.flush()
        given = int(input().strip())
        solres = solving(m1,m1,given)
        if solres == 0:
            print(f"! {m1}")
            continue
        print(f"? {m2} {m2}")
        sys.stdout.flush()
        given = int(input().strip())
        solres = solving(m2,m2,given)
        if solres == 0:
            print(f"! {m2}")
            continue
        print(f"? {m1+1} {m1+1}")
        sys.stdout.flush()
        given = int(input().strip())
        solres = solving(m1,m1,given)
        if solres == 0:
            print(f"! {m1+1}")
            continue
