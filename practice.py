str = str(input())

def ans(str):
    tmp_list = str.split(' ')
    res = []
    for n in tmp_list:
        if len(n) > 3:
            res.append(n)
    return res

print(ans(str))