# ---------------------------------------------------------------------------------------------------- #
# 팩토리얼 0의 개수 

# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.
# ---------------------------------------------------------------------------------------------------- #

def counter_zero(num):
    res = 1
    zero_count = 0
    index = 0

    if num == 0 or num == 1:
        print("0")
    else:
        while (num >= 1):
            res *= num
            num -= 1
        for i, 


        
        print(zero_count)

# main
n = int(input())
counter_zero(n)