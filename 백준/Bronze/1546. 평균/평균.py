import sys

a = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))

max_score = max(score_list)
change_list = [score / max_score * 100 for score in score_list]

print(sum(change_list) / a)
