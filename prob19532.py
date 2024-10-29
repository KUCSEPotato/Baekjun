# ---------------------------------------------------------------------------------------------------- #
# 수학은 비대면강의입니다

# 문제
# ax + by = c
# dx + ey = f 
# 의 연립방정식의 해를 구하시오.

# 입력
# 정수 a, b, c, d, e, f가 공백으로 구분되어 차례대로 주어진다.(-999, 999)
# 문제에서 언급된 방정식을 만족하는 (x, y)가 유일하게 존재하고 [-999, 999] 구간임이 보장된다.

# 출력
# x와 y를 공백으로 구분하여 출력한다.
# ---------------------------------------------------------------------------------------------------- #

# 근의 공식 #
# https://namu.wiki/w/%EC%97%B0%EB%A6%BD%EB%B0%A9%EC%A0%95%EC%8B%9D
        
# main
(a, b, c, d, e, f) = map(int, input().split())

x = (e*c - b*f) // (a*e - b*d)
y = (a*f - d*c) // (a*e - b*d)

print(x, y)