n = int(input())
all_strings = []
for i in range(n):
    s1 = str(input())
    if len(s1) > 10:
        new_string = s1[0] + str((len(s1)-2)) + s1[-1]
        all_strings.append(new_string)
    else:
        all_strings.append(s1)
for i in all_strings:
    print(i)
