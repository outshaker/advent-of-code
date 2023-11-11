f = open('d6-sample.txt',encoding='utf8')
# f = open('d6',encoding='utf8') # github
# f = open('d6.txt',encoding='utf8') # google
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()


def sol(ln):
    for i in range(0, len(ln)-3):
        # print(i, i+3)
        if len(set(ln[i:i+4])) == 4:
            # print(ln[i:i+4], i)
            # print(i + 4)
            return i + 4
            break
    return None

# print(sol(lns[0]))
print(list(map(sol, lns))) # except 7, 5, 6, 10, 11


def sol2(ln):
    for i in range(0, len(ln)-13):
        s = set(ln[i:i+14])
        if len(s) == 14:
            # print(ln[i:i+14],i, i+14)
            # print(i + 14)
            return i + 14
            break
    return None

# print(sol2(lns[0]))
print(list(map(sol2, lns))) # except 19, 23, 23, 29, 26
