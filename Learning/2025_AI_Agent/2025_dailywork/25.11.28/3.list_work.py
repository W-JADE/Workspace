# 1. 평균과 최댓값을 출력해라
scores = [88,92,79,100,86]
total = 0
for s in scores :
    total += s
print(max(scores), min(scores))



# 2. 홀수만 골라 합계를 구하라(반폭문 또는 컴플리헨션)
nums = list(range(1,21))
total = 0 
for nums in nums :
    if nums % 2 == 1 : 
        total += nums
print(total)



# 3. 각 단어의 길이로 구성된 리스트를 생성하라
words = ["AI", "data", "python", "model"]

lengths = [len(w) for w in words]
print(lengths)



# 4. 오름차순 정렬 후 가장 큰 2개만 남겨 새 리스트를 만들어라
views = [120, 98, 450, 310, 260]

views.sort()
result = views[-2 :]
print(result)

'''
=== 결과 ===
100 79
100
[2, 4, 6, 5]
[310, 450]
'''