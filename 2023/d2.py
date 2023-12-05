# f = open('d2-sample.txt',encoding='utf8')
f = open('d2.txt',encoding='utf8') # github
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# Game {g}: {} [blue|green|red] (, 
# X, X; X, X; X

# import re
# pattern = re.compile(r"Game\s*(?P<no>\d+):(\s*;?((?P<pair_i>\d+)\s(?P<pair_c>blue|red|green))(, (?P<pair_i2>\d+)\s(?P<pair_c2>blue|red|green))*;?)+", re.MULTILINE)

# for ln in lns:
  # matches = list(pattern.finditer(ln)) # => dict
  # matches = pattern.findall(ln) # => tuple

  # print(matches)
  # for k,v in matches.items():
    # print(k,v)

# ===== #
from functools import reduce

def toTuple(part):
  n, c = part.split(' ')
  if c == 'red':
    return (int(n), 0, 0)
  elif c == 'green':
    return (0, int(n), 0)
  elif c == 'blue':
    return (0, 0, int(n))

def c(rgb_tuples): return reduce(lambda acc, x: (acc[0] + x[0], acc[1] + x[1], acc[2] + x[2]), rgb_tuples)

def toRGBTuple(parts): return c([toTuple(part) for part in parts])

def chk(rgb_tuple): return 0 <= rgb_tuple[0] <= 12 and 0 <= rgb_tuple[1] <= 13 and 0 <= rgb_tuple[2] <= 14

def f(ln): # check ln is valid
  _, rest = ln.split(': ')
  segments = rest.split('; ')
  for segment in segments:
    parts = segment.split(', ')
    if not chk(toRGBTuple(parts)):
      return False
  return True

# part1
# s = 0
# for i in range(len(lns)):
  # ln = lns[i]
  # if f(ln):
    # print('add', i+1)
    # s += (i+1)
# print(s)



# part2
def c2(rgb_tuples): return reduce(lambda acc, x: (max(acc[0] ,x[0]), max(acc[1], x[1]), max(acc[2],x[2])), rgb_tuples)

def getPower(rgb_tuple): return rgb_tuple[0] * rgb_tuple[1] * rgb_tuple[2]

def g(ln):
  _, rest = ln.split(': ')
  segments = rest.split('; ')
  rgb_tuples = [toRGBTuple(segment.split(', ')) for segment in segments]

  return getPower(c2(rgb_tuples))

s = 0
for i in range(len(lns)):
  ln = lns[i]
  # print(g(ln))
  s += g(ln)

print(s)

