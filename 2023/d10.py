from collections import Counter

toXY = lambda pt: (pt[0], pt[1])
is_valid_pt = lambda x,y: not(x == -1 or x == w or y == -1 or y == h)
test_pt = lambda pt: is_valid_pt(*toXY(pt))
flip = lambda x: (x+1) % 2

def isAccept(next_ptv):
  x, y, to_dir = next_ptv
  _reverse_dir = { 'W': 'S', 'S': 'W', 'A': 'D', 'D': 'A' }
  from_dir = _reverse_dir[to_dir]

  c = lns[y][x]
  if c == '.' or c == 'S': return False

  allowed_from_dir = {
    '|': ['W', 'S'],
    '-': ['A', 'D'],
    'L': ['S', 'D'],
    'J': ['S', 'A'],
    '7': ['W', 'A'],
    'F': ['W', 'D'],
  }

  return from_dir in allowed_from_dir[c]

def getNextDir(this_ptv):
  x, y, to_dir = this_ptv
  c = lns[y][x]
  if c == '.' or c == 'S': return False
  _reverse_dir = { 'W': 'S', 'S': 'W', 'A': 'D', 'D': 'A' }
  from_dir = _reverse_dir[to_dir]

  allowed_to_dir = {
    '|': ['W', 'S'],
    '-': ['A', 'D'],
    'L': ['S', 'D'],
    'J': ['S', 'A'],
    '7': ['W', 'A'],
    'F': ['W', 'D'],
  }
  i = flip(allowed_to_dir[c].index(from_dir))

  return allowed_to_dir[c][i]

def _getNextPtv(pt, dir):
  x, y = pt
  nx, ny = None, None
  if dir == 'W':
    nx, ny = x, y+1
  elif dir == 'S':
    nx, ny = x, y-1
  elif dir == 'A':
    nx, ny = x-1, y
  elif dir == 'D':
    nx, ny = x+1, y

  if not is_valid_pt(nx, ny): return None

  return (nx, ny, dir)

def getNextPtv(this_ptv):
  # print('getNextPtv', this_ptv)
  this_pt, this_dir = (this_ptv[0], this_ptv[1]), this_ptv[2]
  next_dir = getNextDir(this_ptv)
  # print('getNextPtv, next_dir', next_dir)
  next_ptv = _getNextPtv(this_pt, next_dir)
  # print('getNextPtv, next_ptv', next_ptv)

  return next_ptv

def checkSide(bd, this_ptv):
  x, y, to_dir = this_ptv
  c = lns[y][x]
  if c == 'S': return
  _reverse_dir = { 'W': 'S', 'S': 'W', 'A': 'D', 'D': 'A' }
  from_dir = _reverse_dir[to_dir]

  _pat = {
    'W|':" R L",
    'WF':"L  L",
    'W7':"RR  ",

    'S|':" L R",
    'SJ':" LL ",
    'SL':"  RR",

    'A-':"L R ",
    'A7':"LL  ",
    'AJ':" RR ",

    'D-':"R L ",
    'DF':"R  R",
    'DL':"  LL",
  }
  pats = _pat[from_dir + c]
  pts = [(x,y-1),(x+1,y),(x,y+1), (x-1,y)]
  for i in range(4):
    pat, pt = pats[i], pts[i]
    x,y = pt[0], pt[1]
    if pat != ' ' and is_valid_pt(x,y) and bd[y][x] == '.':
      bd[y][x] = pat


def show(bd):
  for j in range(h):
    for i in range(w):
      print(bd[j][i], end='')
    print('')
  print('')

# NOTE 這邊所有的座標方位
# 正眼下 W (x,y+1)
# 正眼上 S (x,y-1)
# 正眼左 A (x-1,y)
# 正眼右 D (x+1,y)


# f = open('d10-sample.txt',encoding='utf8')
# f = open('d10-2-1.txt',encoding='utf8')
# f = open('d10-2-2.txt',encoding='utf8')
# f = open('d10-2-3.txt',encoding='utf8')
f = open('d10.in',encoding='utf8') # github

lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

w, h = len(lns[0]), len(lns)

bd = [['.' for i in range(w)] for j in range(h)]

for j in range(h):
  for i in range(w):
    if lns[j][i] == 'S':
      start_pt = (i, j)

start_x, start_y = start_pt
bd[start_y][start_x] = 'S'
print('start from', start_pt) # step 0
next_ptvs = [
  (start_x+1, start_y, 'D'),
  (start_x-1, start_y, 'A'),
  (start_x, start_y+1, 'W'),
  (start_x, start_y-1, 'S')
]
next_ptvs = list(filter(lambda ptv: test_pt(ptv) and isAccept(ptv), next_ptvs)) # two way
print('next_ptvs', next_ptvs)
this_ptv = next_ptvs[0] # choose one way to go
first_ptv = next_ptvs[0]
bd[this_ptv[1]][this_ptv[0]] = 'x'
# print('this_ptv', this_ptv)# step 1
step = 1
is_end = lambda ptv: (ptv[0], ptv[1]) == start_pt
while not is_end(this_ptv):
  this_ptv = getNextPtv(this_ptv)
  bd[this_ptv[1]][this_ptv[0]] = 'x'
  # print('this_ptv', this_ptv)
  step += 1

cycle_n = step
print('cycle_n', cycle_n)
print('part1 ans', step/2) # part1 ans

show(bd)

this_ptv = first_ptv
# print('this_ptv', this_ptv)
checkSide(bd, this_ptv)
for i in range(cycle_n):
  this_ptv = getNextPtv(this_ptv)
  if this_ptv == (None, None, False): break
  # print('this_ptv', this_ptv)
  checkSide(bd, this_ptv)

show(bd)

_all_tile = ''.join([''.join(ln) for ln in bd])
c = Counter(_all_tile)
L_n = c.get('L')
R_n = c.get('R')
print(min(R_n, L_n))






