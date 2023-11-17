# f = open('d10-sample.txt',engcoding='utf8')
f = open('d10-sample-2.txt',encoding='utf8')
# f = open('d10',encoding='utf8') # github
# f = open('d10.txt',encoding='utf8')
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

tick_log = []
tick = 1
reg = 1
for ln in lns:
  if ln.startswith('noop'):
    tick += 1
    tick_log.append((tick, reg))
  elif ln.startswith('addx'):
    cmd, val = ln.split()
    tick += 2
    reg += int(val)
    tick_log.append((tick, reg))

# print(tick_log)


def find_(tick_log, tick_no):
  match_log = list(filter(lambda log: tick_no == log[0], tick_log)) or list(filter(lambda log: tick_no - 1 == log[0], tick_log))
  print(match_log)
  if len(match_log) == 1: return match_log[0][1]

def part1():
  r = [find_(tick_log, tick_no) * tick_no for tick_no in range(20, 221, 40)]
  print(r, sum(r))

def part2():
  tick_dict = {}
  tick_array = []
  for i in range(len(tick_log)):
    k, v = tick_log[i]
    tick_dict[k] = v
  # print(tick_dict)

  reg = 1
  for i in range(1, 241): # 1 ~ 240
    if tick_dict.get(i):
      tick_array.append(tick_dict[i])
      reg = tick_dict[i]
    else:
      tick_array.append(reg)
  # print(tick_array)

  for i in range(240): # 0 ~ 239
    position = i % 40
    sprite_position = tick_array[i]

    if abs(sprite_position -position) <= 1:
      print('#', end='')
      # print('*', end='') # looks friendly
    else:
      print('.', end='')
      # print(' ', end='') # looks friendly

    if i % 40 == 39: print('')

part1()
print('')
part2()
