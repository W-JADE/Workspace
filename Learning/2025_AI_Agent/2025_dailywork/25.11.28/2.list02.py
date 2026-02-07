'''
맨 뒤에 추가      |	append(x)	 | 한 개 추가	    | scores.append(60)
여러 개 이어붙이기 | extend(리스트)| 리스트 병합       | scores.extend([85, 77])
원하는 위치에 삽입 | insert(i, x) |	i번 자리에 x 삽입 | scores.insert(1, 88)
값으로 삭제	      | remove(x)	 | 첫 x 삭제	    | scores.remove(70)
위치로 삭제	      | pop(i)	     | i번 원소 꺼내 삭제| scores.pop(0)
전체 비우기	      | clear()	     | 모두 삭제	    | scores.clear()
제자리 정렬	      | sort()	     | 오름차순 정렬	 | scores.sort()
정렬된 새 리스트   | sorted(리스트)| 원본 보존	      | sorted(scores, reverse=True)

'''

# 1. 추가하기
scores = [80, 90]
scores.append(100)     # 뒤에 100 추가
scores.insert(1, 85)   # 1번 자리에 85 넣기
#>> [80, 85, 90, 100]

# 2.삭제하기
scores.remove(90)      # 값으로 삭제
scores.pop(0)          # 0번 자리 삭제
#>> [85, 100]

# 3. 정렬하기
scores = [90, 70, 100]
scores.sort()          # 작은 수 → 큰 수
#>> [70, 90, 100]

# 리스트는 복사해서 넣을 때 주의해야 한다
# 4. 한줄로 만들기_리스트컴프리헨션
numbers = [1, 2, 3, 4, 5]
double_numbers = [n * 2 for n in numbers]
#>> [2, 4, 6, 8, 10]