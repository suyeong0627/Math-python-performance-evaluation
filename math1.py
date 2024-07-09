import sympy as sp

def solve_sin_equation():
    # 사용자로부터 y 값을 입력받음
    y_input = input("주어진 sin(x) 값(y)을 입력하세요 (-1에서 1 사이, 루트를 입력하고 싶다면, 예: sqrt(2)/2): ")

    # 수식을 변환
    try:
        y = sp.sympify(y_input)
    except sp.SympifyError:
        print("입력한 값이 올바른 형식의 수식이 아닙니다. 다시 입력해주세요.")
        return
    
    # y 값이 유효한지 확인 (-1에서 1 사이의 값이어야 함)
    if not -1 <= y <= 1:
        print("주어진 y 값이 유효하지 않습니다. -1에서 1 사이의 값을 입력해주세요.")
        return
    
    # arcsin(y)를 계산하여 x를 구함 (단위는 라디안)
    x1 = sp.asin(y)
    x2 = sp.pi - x1
    
    # 0 <= x < 2π 범위 내의 값을 찾기 위해 주기성을 고려
    solutions = []
    for k in range(-1, 2):  # 주기성을 고려하여 k를 -1부터 1까지
        x1_k = x1 + 2 * sp.pi * k
        x2_k = x2 + 2 * sp.pi * k
        if 0 <= x1_k < 2 * sp.pi:
            solutions.append(x1_k)
        if 0 <= x2_k < 2 * sp.pi:
            solutions.append(x2_k)
    
    # 결과 출력
    print(f"sin(x) = {y}")
    for sol in solutions:
        pi_fraction = sol / sp.pi
        print(f"x = {sol.evalf()} radians ({pi_fraction} * π radians)")

# 함수 호출
solve_sin_equation()
