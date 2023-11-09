f = open('d4-sample.txt',encoding='utf8')
# f = open('d4.txt',encoding='utf8')
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

def pack(ln): return ln.split(',')
def pack2(secs): return list(map(lambda sec: list(map(int, sec.split('-'))), secs))

def isCovered(s):
    # print(s[0], s[1])
    return (s[0][0] <= s[1][0] and s[0][1] >= s[1][1]) or (s[1][0] <= s[0][0] and s[1][1] >= s[0][1])

def isOverlap(s):
    return not ((s[0][0] < s[1][1]) and (s[0][1] < s[1][0])) and not ((s[0][0] > s[1][1]) and (s[0][1] > s[1][0]))

def sol(ln): return 1 if isCovered(pack2(pack(ln))) else 0
def sol2(ln): return 1 if isOverlap(pack2(pack(ln))) else 0

def part1():
  print(sum(map(sol, lns)))

def part2():
  print(sum(map(sol2, lns)))

part1() # except 2
part2() # except 4