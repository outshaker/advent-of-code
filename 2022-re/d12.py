# f = open('d12-sample.txt',encoding='utf8')
# f = open('d12',encoding='utf8') # github
f = open('d12.txt',encoding='utf8')
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()


from functools import reduce

is_first_time = lambda pt: vis[pt[1]][pt[0]] == None

def view(land, vis, next_pts = set()):
  w, h = len(land[0]), len(land)
  for j in range(h):
    # print(vis[j])
    for i in range(w):
      if (i,j) in next_pts:
        print('N', end='')
      elif (i, j) == (goal_pt[0], goal_pt[1]):
        print('E', end='')
      elif vis[j][i] == None:
        print('.', end='')
        # print(land[j][i], end='')
      elif vis[j][i] != None:
        # print('#', end='') # old style
        print(vis[j][i] % 10, end='')
      else:
        print('.', end='')
    print('')

w, h = len(lns[0]), len(lns)
land = [list(ln) for ln in lns]
vis = [[None for i in range(w)] for j in range(h)]


for j in range(h):
  for i in range(w):
    if land[j][i] == 'S':
      start_pt = (i, j)
    if land[j][i] == 'E':
      goal_pt = (i, j)
# print(start_pt, goal_pt)


def part1():
  def getNextPts(origin_pt, land, vis):
    x, y, w, h = origin_pt[0], origin_pt[1], len(land[0]), len(land)
    is_valid_pt = lambda pt: (0 <= pt[0] < w) and (0 <= pt[1] < h)  
    base_level = ord(land[origin_pt[1]][origin_pt[0]])
    get_level = lambda pt: 97 if land[pt[1]][pt[0]] == 'S' else (122 if land[pt[1]][pt[0]] == 'E' else ord(land[pt[1]][pt[0]])) # a => 97, z=> 122
    is_valid_lv = lambda pt: get_level(pt) in (get_level(origin_pt), get_level(origin_pt) + 1) or get_level(pt) < get_level(origin_pt)
    pts = list(filter(lambda pt: is_valid_pt(pt) and is_valid_lv(pt) and is_first_time(pt), [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]))

    return pts


  vis[start_pt[1]][start_pt[0]] = 0 # set start
  this_pts = [start_pt]

  _n = [getNextPts(pt, land, vis) for pt in this_pts]
  next_pts = reduce(lambda x, y: set(x) | set(y), _n, set())
  # print(next_pts)

  step = 1
  for pt in next_pts:
    x, y = pt[0], pt[1]
    vis[y][x] = step
  step += 1
  # view(land, vis, next_pts) # 84 x 41

  while len(next_pts) > 0:
    # print(len(next_pts), next_pts)
    # if step % 25 == 0:
      # view(land, vis, next_pts)
      # print('')
      # input(f'step: {step} enter any key')

    this_pts = next_pts
    _n = [getNextPts(pt, land, vis) for pt in this_pts]
    # print('_n', _n)
    next_pts = reduce(lambda x, y: set(x) | set(y), _n, set())
    # print(next_pts)

    # add to visisted pts
    for pt in next_pts:
      x, y = pt[0], pt[1]
      vis[y][x] = step

    # view(land, vis, next_pts)
    # print('')

    # check ending # part1
    if vis[goal_pt[1]][goal_pt[0]] != None:
      print('reach to goal')
      view(land, vis, next_pts)
      break
    else:
      step += 1

  view(land, vis, next_pts)
  print(step) # total step, -1 to fix last update


def part2():
  def getNextPts(origin_pt, land, vis):
    x, y, w, h = origin_pt[0], origin_pt[1], len(land[0]), len(land)
    is_valid_pt = lambda pt: (0 <= pt[0] < w) and (0 <= pt[1] < h)  
    base_level = ord(land[origin_pt[1]][origin_pt[0]])
    get_level = lambda pt: 97 if land[pt[1]][pt[0]] == 'S' else (122 if land[pt[1]][pt[0]] == 'E' else ord(land[pt[1]][pt[0]])) # a => 97, z=> 122
    is_valid_lv = lambda pt: get_level(pt) in (get_level(origin_pt), get_level(origin_pt) - 1) or get_level(pt) > get_level(origin_pt)
    pts = list(filter(lambda pt: is_valid_pt(pt) and is_valid_lv(pt) and is_first_time(pt), [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]))

    return pts


  vis[goal_pt[1]][goal_pt[0]] = 0 # set start
  this_pts = [goal_pt]
  _n = [getNextPts(pt, land, vis) for pt in this_pts]
  next_pts = reduce(lambda x, y: set(x) | set(y), _n, set())
  # print(next_pts)

  step = 1
  for pt in next_pts:
    x, y = pt[0], pt[1]
    vis[y][x] = step
  step += 1
  # view(land, vis, next_pts) # 84 x 41

  is_part2_end = False # part2

  while len(next_pts) > 0:
    # print(len(next_pts), next_pts)
    # if step % 25 == 0:
      # view(land, vis, next_pts)
      # print('')
      # input(f'step: {step} enter any key')

    this_pts = next_pts
    _n = [getNextPts(pt, land, vis) for pt in this_pts]
    # print('_n', _n)
    next_pts = reduce(lambda x, y: set(x) | set(y), _n, set())
    # print(next_pts)

    # add to visisted pts
    for pt in next_pts:
      x, y = pt[0], pt[1]
      vis[y][x] = step

    # view(land, vis, next_pts)
    # print('')


    # check ending
    step += 1
    for pt in next_pts:
      x, y = pt[0], pt[1]
      if land[y][x] == 'a':
        is_part2_end = True
        step -= 1
        break
    if is_part2_end: break


  view(land, vis, next_pts)
  print(step) # total step, -1 to fix last update

# choose one to exec
# part1()
part2()
