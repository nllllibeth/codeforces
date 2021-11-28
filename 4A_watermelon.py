def weight_div(w):
    if w >= 4:
        if w % 2 == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
a = int(input())
print(weight_div(a))