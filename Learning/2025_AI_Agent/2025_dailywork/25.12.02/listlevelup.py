# 리스트 레벨 업 심화해보기
'''
days =[31,28,31,30,31,30,31,31,30,31,30,31] #리스트 준비
1. 12달의 요소값을 total에 누적해서 출력해보기
2. 4월 ~ 8월 까지의 날짜를 while문으로 누적해본다
3. for문으로도 누적해 본다 (흰트 : 슬라이스 기법(:))

'''

# 월의 날짜수를 저장하는 리스트 준비
days =[31,28,31,30,31,30,31,31,30,31,30,31]
print(len(days))
print(days)

# 1. 12달의 요소값을 total에 누적해서 출력해보기
total = 0 # for문을 사용
for day in days :
    total += day
print("total:", total)

# 2. 4월 ~ 8월 까지의 날짜를 while문으로 누적해본다
# 직접 해본 것 : 4월 ~ 8월 까지의 날짜를 while문으로 누적해본다
total = 0
i = 3   
while i <= 7:   
    total += days[i]
    print(days[i])
    i += 1

print("총 날짜의 합 =", total)


# 3. for문으로도 누적해 본다 (흰트 : 슬라이스 기법(:))
# 직접해본 것 : for문으로도 누적해 본다 (흰트 : 슬라이스 기법(:))
total = 0
for d in days[3:8]: 
    total += days
    print(days)

print("총 날짜의 합 =", total)

# 강사님이 설명해 주신 방법 - 1. range를 사용하는 방법
total = 0
startMonth = 4
endMonth = 8
for i in range(startMonth-1, endMonth) :
    print(days[i])
    total += days[i]

print(f"{startMonth}부터 {endMonth}까지의 총 날짜는 {total}입니다.")

# 강사님이 설명해 주신 방법 - 2.for문과 슬라이싱을 묶어서 사용
total = 0
for day in days[startMonth-1 : endMonth] :
    print(day)
    total += day
print(total)

