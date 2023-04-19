# # pdf 79페이지
#
# import time
#
# number = 0
#
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1
#
#
# print(f"5초동안 {number}번 반복했습니다.")
#

# 93페이지 가변매개변수 / 가변매개변수는 튜플 타입으로 돼있다.

# 기본매개변수와 키워드 매개변수를 자주 사용한다 머신러닝에서

## 팩토리얼 만들기

# for문 이용
def factorial_repeat(n):
    num = 1
    result = 1
    while num <= n:
        result *= num
        num += 1
    return result


print("반복문으로 팩토리얼")
print("1!:", factorial_repeat(1))
print("2!:", factorial_repeat(2))
print("3!:", factorial_repeat(3))
print("4!:", factorial_repeat(4))
print("5!:", factorial_repeat(5))



# recursion을 이용

def factorial_recursion(n):
    result = n * factorial_repeat(n-1)
    return result


print("\n\n재귀함수로 팩토리얼")
print("1!:", factorial_recursion(1))
print("2!:", factorial_recursion(2))
print("3!:", factorial_recursion(3))
print("4!:", factorial_recursion(4))
print("5!:", factorial_recursion(5))

