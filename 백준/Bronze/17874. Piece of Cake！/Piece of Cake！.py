n, h, v = map(int, input().split())


p1 = h * v
p2 = h * (n - v)
p3 = (n - h) * v
p4 = (n - h) * (n - v)

max_piece = max(p1, p2, p3, p4)

print(max_piece * 4)