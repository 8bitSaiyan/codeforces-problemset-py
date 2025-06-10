n = int(input())
count = 0
for _ in range(n):
    op = input()
    if "++" in op:
        count += 1
    elif "--" in op:
        count -=1
        
print(count)