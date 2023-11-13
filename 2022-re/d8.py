f = open('d8-sample.txt',encoding='utf8')
# f = open('d8',encoding='utf8') # github
# f = open('d8.txt',encoding='utf8') # google
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

array = [[int(x) for x in ln] for ln in lns]
w, h = len(lns[0]), len(lns) # j, i

# part1
visible = [[False for j in range(w)] for i in range(h)]
# print(array)
# print(visible)

# outside tree is visible
for i in range(h):
  visible[i][0] = True
  visible[i][-1] = True
for j in range(w):
  visible[0][j] = True
  visible[-1][j] = True

# view up to down
for j in range(1, w-1):
  s = array[0][j] # start
  for i in range(1, h-1):
    if array[i][j] > s:
      # print(f'({i},{j}) [{array[i][j]}] > {s}')
      s = array[i][j]
      visible[i][j] = True

# view down to up
for j in range(1, w-1):
  s = array[-1][j] # start
  for i in range(h-2, 0, -1):
    if array[i][j] > s:
      # print(f'({i},{j}) [{array[i][j]}] > {s}')
      s = array[i][j]
      visible[i][j] = True

# view left to right
for i in range(1, h-1):
  s = array[i][0] # start
  for j in range(1, w-1):
    if array[i][j] > s:
      # print(f'({i},{j}) [{array[i][j]}] > {s}')
      s = array[i][j]
      visible[i][j] = True

# view right to left
for i in range(1, h-1):
  s = array[i][-1] # start
  # print('s', s)
  for j in range(w-2, 0, -1):
    if array[i][j] > s:
      # print(f'({i},{j}) [{array[i][j]}] > {s}')
      s = array[i][j]
      visible[i][j] = True

r = sum([sum(map(lambda x: 1 if x else 0, ln)) for ln in visible])
print(r)

# part2
r2 = 0
for px in range(1, w-1): # px 1 to w-2
  for py in range(1, h-1): # py 1 to h-2
    height = array[py][px]

    # go up (i,j) => (0, j) 1
    cout_up = 0
    j = px
    for i in range(py-1, -1, -1):
      # print('i', i)
      # print('height', height, array[i][j])
      # if height >= array[i][j]:
      cout_up += 1
      if height <= array[i][j]:
        break
    # print('cout_up', cout_up)
    # if cout_up == 0: continue

    # go down (i,j) => (h-1, j) 2
    cout_down = 0
    for i in range(py + 1, h):
      # print('i', i)
      # print('height', height, array[i][j])
      # if height >= array[i][j]:
      cout_down += 1
      if height <= array[i][j]:
        break
    # print('cout_down', cout_down)
    # if cout_down == 0: continue

    # go left (i,j) => (i, 0) 1
    cout_left = 0
    i = py
    for j in range(px-1, -1, -1):
      # print('j', j)
      # print('height', height, array[i][j])
      # if height >= array[i][j]:
      cout_left += 1
      if height <= array[i][j]:
        break
    # print('cout_left', cout_left)
    # if cout_left == 0: continue

    # go right (i,j) => (i, w-1) 2
    cout_right = 0
    for j in range(px + 1, w):
      # print('j', j)
      # print('height', height, array[i][j])
      # if height >= array[i][j]:
      cout_right += 1
      if height <= array[i][j]:
        break
    # print('cout_right', cout_right)
    # if cout_right == 0: continue

    # print(px, py, height, cout_up * cout_left * cout_right * cout_down)
    if cout_up * cout_left * cout_right * cout_down > r2:
      r2 = cout_up * cout_left * cout_right * cout_down
      print(f'add ({px}, {py})', r2)

print(r2)