f = open('d1-sample.txt',encoding='utf8')
# f = open('d1.txt',encoding='utf8')
full = f.read()
f.close()

def pack(s):
    lst = s.split('\n')
    return sum(map(int, lst))

def part1():
    parts = full.split('\n\n')
    ls = list(map(pack, parts))
    print(max(ls))

def part2():
    parts = full.split('\n\n')
    ls = list(map(pack, parts))
    ls.sort(reverse=True)
    print(sum(ls[0:3]))

part1() # except 24000
part2() # except 45000
