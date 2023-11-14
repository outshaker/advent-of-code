# f = open('d9-sample.txt',encoding='utf8')
f = open('d9-sample-2.txt',encoding='utf8')
# f = open('d9',encoding='utf8') # github
# f = open('d9.txt',encoding='utf8') # google
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

# generate pt in path
def to(start_pt, dir_, n):
  path = []

  if dir_ == 'U':
    vet = (0, 1)
  elif dir_ == 'D':
    vet = (0, -1)
  elif dir_ == 'R':
    vet = (1, 0)
  elif dir_ == 'L':
    vet = (-1, 0)

  for x in range(n): # repeat n times
    next_pt = (start_pt[0] + vet[0], start_pt[1] + vet[1])
    path.append(next_pt)
    start_pt = next_pt

  return start_pt, path

def get_head_log(lines):
  head_pt = (0,0) # start point
  head_log = []
  head_log.append(head_pt)
  for line in lines:
    dir_, n = line.split()
    head_pt, path = to(head_pt, dir_, int(n))
    head_log.extend(path)

  # print(head_log)
  return head_log

def is_around(pt_a, pt_b): return abs(pt_a[0]-pt_b[0]) <= 1 and abs(pt_a[1]-pt_b[1]) <= 1

def get_next_pt(pt_now, pt_next):
  x_diff = pt_next[0] - pt_now[0]
  dx = 1 if x_diff >= 1 else (0 if x_diff == 0 else -1)
  y_diff = pt_next[1] - pt_now[1]
  dy = 1 if y_diff >= 1 else (0 if y_diff == 0 else -1)

  pt_now_x, pt_now_y = pt_now
  if (dx, dy) == (1, 1): return (pt_now_x + 1, pt_now_y + 1)
  elif (dx, dy) == (-1, 1): return (pt_now_x - 1, pt_now_y + 1)
  elif (dx, dy) == (-1, -1): return (pt_now_x - 1, pt_now_y - 1)
  elif (dx, dy) == (1, -1): return (pt_now_x + 1, pt_now_y - 1)

  elif (dx, dy) == (1, 0): return (pt_now_x + 1, pt_now_y)
  elif (dx, dy) == (0, 1): return (pt_now_x, pt_now_y + 1)
  elif (dx, dy) == (-1, 0): return (pt_now_x - 1, pt_now_y)
  elif (dx, dy) == (0, -1): return (pt_now_x, pt_now_y - 1)

def get_tail_log(head_log):
  tail_pt = head_log[0]
  tail_log = []
  tail_log.append(tail_pt)
  for head_pt in head_log:
    if is_around(tail_pt, head_pt):
      pass
    else:
      tail_pt = get_next_pt(tail_pt, head_pt)
      tail_log.append(tail_pt)

  # print(tail_log)
  return tail_log

def show(visited_pt):
  w_min = min(map(lambda pt: pt[0], visited_pt))
  w_max = max(map(lambda pt: pt[0], visited_pt))
  h_min = min(map(lambda pt: pt[1], visited_pt))
  h_max = max(map(lambda pt: pt[1], visited_pt))
  
  print(f'x from {w_min} to {w_max}')
  print(f'y from {h_min} to {h_max}')

  for y in range(h_max, h_min-1, -1):
    for x in range(w_min, w_max+1):
      if (x,y) == (0,0): print('s', end = '')
      else: print('#' if (x,y) in visited_pt else '.', end = '')
    print('')

head_log = get_head_log(lns)
# print(head_log)

# part1
def part1(head_log):
  tail_log = get_tail_log(head_log)
  visited_pt = set(tail_log)
  # print(visited_pt, len(visited_pt))
  r = len(visited_pt)
  print(r)
  # show(visited_pt)


# part2
def part2(head_log):
  # show(set(head_log)) # head log

  iter_tail_log = get_tail_log(head_log) # first time
  # print('iter_tail_log#1', iter_tail_log)
  iter_visited_pt = set(iter_tail_log)
  # show(iter_visited_pt) # iter tail log
  # print(iter_visited_pt, len(iter_visited_pt))
  r = len(iter_visited_pt)
  # print(r)

  for i in range(2, 10): # last 8 times
    iter_tail_log = get_tail_log(iter_tail_log)
    # print(f'iter_tail_log#{i}', iter_tail_log)
    iter_visited_pt = set(iter_tail_log)
    # show(iter_visited_pt) # iter tail log
    # print(iter_visited_pt, len(iter_visited_pt))
    r = len(iter_visited_pt)
    print(r)

# part1(head_log)
part2(head_log)
