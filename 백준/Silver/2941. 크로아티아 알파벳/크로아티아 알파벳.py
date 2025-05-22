a = input()
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

if any(b in a for b in b):
    for i in b:
        a = a.replace(i, i[0])

print(len(a))