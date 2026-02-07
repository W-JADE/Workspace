# if 문은 조건문 중 가장 단순하면서도 중요한 구조!
# 조건식이 참일 경우에만 코드 블록이 실행됨
# 파이썬에서는 조건문이 끝날 때 콜론(:)을 반드시 붙임
# 실행문은 들여쓰기(보통 공백 4칸)로 구분 (핵심!)

temperature = 30
if temperature > 25:
    print("날씨가 덥습니다.")
'''
등분: a == b
동등하지 않음: a != b
미만: < b
작음 이하: a <= b
보다 크다: a > b
크거나 같다면: a >= b
'''

age = 30
if age >= 20:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")