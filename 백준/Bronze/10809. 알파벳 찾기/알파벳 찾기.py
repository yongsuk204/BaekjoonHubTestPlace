upper_dict = {chr(i + 97): i for i in range(26)}

list_1 = [-1] * 26

for idx, i in enumerate(input()):
    if list_1[upper_dict[i]] == -1:
        list_1[upper_dict[i]] = idx

print(" ".join(map(str,list_1)))