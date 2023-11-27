# f = open('d13-sample.txt',encoding='utf8')
# f = open('d13',encoding='utf8') # github
f = open('d13.txt',encoding='utf8')
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

from math import ceil
from functools import cmp_to_key

def toList(x): return [x] if type(x) is int else x

def cmp_num(L, R):
  # print('cmp_num', L, R)
  if L < R: return 1
  elif L > R: return -1
  else: return 0 # pass to next

def cmp_list(L, R):
  # print('cmp_list', L, R)
  pairs = list(zip(L, R))
  # print('pairs', pairs)
  for pair in pairs:
    x, y = pair
    r = cmp(x, y)
    if r != 0: return r

  if len(L) < len(R): return 1
  elif len(L) > len(R): return -1
  else: return 0 # pass to next

def cmp(L, R):
  # print('cmp', L, R)
  if type(L) is int and type(R) is int:
    # print('case 1')
    return cmp_num(L, R)
  elif type(L) is list and type(R) is list:
    # print('case 2')
    return cmp_list(L, R)
  else:
    # print('case 3')
    return cmp_list(toList(L), toList(R))


def part1():
  cout = 0
  n = ceil(len(lns) / 3)
  for i in range(n):
    L , R = eval(lns[3 * i]), eval(lns[3 * i + 1])
    r = cmp(L, R)
    if r == 1:
      # print('right', i)
      cout += (i+1)

  print(cout)

  # s = sum([i if cmp(eval(lns[3*i]), eval(lns[3*i+1])) == True else 0 for i in range(ceil(len(lns) / 3))])
  # print(s)

def part2():
  x = list(filter(lambda x: x != '', lns))
  x.extend(['[[2]]', '[[6]]'])
  x = list(map(eval, x))
  # for xx in x:
    # print(xx)
  # print('')

  x.sort(key=cmp_to_key(cmp), reverse=True)
  for xx in x: print(xx)
  for i in range(len(x)):
    if repr(x[i]) == '[[2]]': a = i+1
    elif repr(x[i]) == '[[6]]': b = i+1
  print(a, b, a*b)

# choose one to exec
part1()
part2()