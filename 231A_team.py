# With many variables, high run time:
 
# rows = int(input())
# count = 0
# for _ in range(rows):
#     cols = input()
#     a, b, c = map(int, cols.split())
#     if(sum([a, b, c]) >=2):
#         count +=1
# print(count)

# Optimised Approach:
rows = int(input())
count = 0
for _ in range(rows):
    if(sum(map(int, input().split())) >=2):     
        count +=1

print(count)