from re import compile, match, search
from math import lcm

def parse(link_str):
  pat = compile(r"(\w+) = \((\w+), (\w+)\)")
  m = pat.match(link_str)

  return m.groups() if m else None

# for part2
is_XXA = lambda k: match('\w\wA', k) != None
is_XXZ = lambda k: match('\w\wZ', k) != None

# is_end_node = lambda k: k == 'ZZZ' # part1
is_end_node = lambda k: is_XXZ(k)  # part2

def cmd_seq(cmds):
  i = 0
  while True:
    yield cmds[i]
    i =  (i+1) % len(cmds)

# ================================================== #

# f = open('d8-sample.txt',encoding='utf8')
# f = open('d8-sample-2.txt',encoding='utf8')
# f = open('d8-sample-3.txt',encoding='utf8')
f = open('d8.txt',encoding='utf8') # github

lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()



cmds, link_strs = lns[0], lns[2:]

network = {}
for link_str in link_strs:
  node, L_next, R_next = parse(link_str)
  # print(node, L_next, R_next)
  network[node] = (L_next, R_next)

# print(network)





def go(network, start_node = 'AAA', end_test = is_end_node):
  if not network.get(start_node):
    print(f'network has no start_node "{start_node}"')
    return
  this_node = start_node
  step = 0
  for cmd in cmds:
    # print(cmd)
    i = 0 if cmd == 'L' else 1 # L toggle
    next_node = network[this_node][i]
    print(f'{this_node} => {next_node}')
    this_node = next_node
    step += 1

    if is_end_node(this_node): break

  return step, this_node

def part1(network):
  step, this_node = go(network)
  while not is_end_node(this_node):
    add_step, this_node = go(network, this_node)
    step += add_step

  print('step', step)
# part1(network)



def go2(network, _g, start_node = 'AAA'):
  if not network.get(start_node):
    print(f'network has no start_node "{start_node}"')
    return
  this_node = start_node
  step = 0
  for cmd in _g:
    # print(cmd)
    i = 0 if cmd == 'L' else 1 # L toggle
    next_node = network[this_node][i]
    # print(f'{this_node} => {next_node}')
    this_node = next_node
    step += 1

    if is_end_node(this_node): break
    if step > 1e6:
      print('!!!!!!')
      break

  return step, this_node






start_nodes = list(filter(is_XXA, network.keys()))
print(start_nodes)

def get_step(node):
  _g = cmd_seq(cmds)
  step, _z = go2(network, _g, node)
  # step2, _z2 = go2(network, _g, _z)
  # print(node, step, step2, _z, _z2)
  
  return step

steps = [get_step(node) for node in start_nodes]
print(steps)
print(lcm(*steps))

