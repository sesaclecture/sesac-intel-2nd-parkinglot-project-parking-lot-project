"""
Implement User Management System
"""

def make_parking():
    parking = {}
    # 층 만들기
    for f in range(1, FLOORS+1):
        f_name = str(f) + "f"
        # 층 이름
        f_map = {} # 층 딕셔너리

        for r in range(1, ROWS+1):
            # 세로줄 만들기
            for c in range(1, COLS+1):
                # 가로줄 마늗릭
                if r == 2:   # 통로
                    f_map[(r,c)] = " "
                else:        # 주차 가능 자리
                    f_map[(r,c)] = EMPTY

        parking[f_name] = f_map
    return parking

def viewer(parking, floor):
    # 전체를 볼지 한 층만을 볼지
    if not floor:
        # 전체 층 보기(아무것도 입력 x)
        floors = parking.keys()
    else:
        floors = [str(floor) + "f"]

    for f in floors:
        # 실제 뷰어
        print("[" + f + "]")
        for r in range(1, ROWS+1):
            #세로 반복
            line = ""
            for c in range(1, COLS+1):
                # 가로 반복
                line += parking[f][(r,c)]
            print(line)
        print()

#실행(예시)
p = make_parking()
#전체 층 보기(input으로 입력 받기)
a = input('층을 입력하세요(전체 층은 빈칸 or 0 입력 : ')
viewer(p, a)

