# f = open('d3-sample.txt',encoding='utf8')
f = open('d3.txt',encoding='utf8')
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

def toN(x):
  assert len(x) == 1
  if x >= 'a' and x <= 'z': return ord(x) - ord('a') + 1
  elif x >= 'A' and x <= 'Z': return ord(x) - ord('A') + 27
  else:
    # print(x) # debug
    raise ValueError('x not in [a-zA-Z]')

def sol(ln):
  s1, s2 = ln[:len(ln)//2], ln[len(ln)//2:]
  misstake = set(s1) & set(s2)
  # print(s1, s2, misstake) # debug
  assert len(misstake) == 1
  return toN(misstake.pop())

def part1():
  print(sum(map(sol, lns)))

def sol2(ln_3):
    badge = set(ln_3[0]) & set(ln_3[1]) & set(ln_3[2])
    assert len(badge) == 1
    return toN(badge.pop())

def part2():
    chunks = [lns[i:i+3] for i in range(0, len(lns) - 1, 3)]
    print(sum(map(sol2, chunks)))

part1() # except 157
part2() # except 70
