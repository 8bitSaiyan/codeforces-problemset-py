n, k = map(int, input().split())
count = 0

markList = list(map(int, input().split()))

kth_score = markList[k-1]

for marks in markList:
    if marks >= kth_score and marks > 0:
        count += 1
        
print(count)