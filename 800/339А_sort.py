a = [int(i) for i in input().split('+')]
def right_order(s):
    s1, s2, s3 = 0, 0, 0
    for i in s:
        if i == 1:
            s1 += 1
        elif i == 2:
            s2 += 1
        else:
            s3 += 1
    icon = str(("1" * s1) + ("2" * s2) + ("3" * s3))
    print("+".join(icon))
right_order(a)


