a,b = map(int, input().split())
score = 0
for _ in range(2):
    score += max(map(int, input().split()))
print(score)