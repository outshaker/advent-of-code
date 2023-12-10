# f = open('d9-sample.txt',encoding='utf8')
f = open('d9.txt',encoding='utf8') # github

lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

def part1():
  _ = []
  for i in range(len(lns)):
    _seqs = []
    seq = list(map(int, lns[i].split(' ')))
    _seqs.append(seq)
    seq = [seq[i+1] - seq[i] for i in range(0, len(seq)-1)]
    _seqs.append(seq)
    # while not all([s == 0 for s in seq]):
    while sum(seq) != 0: # NOTE: has edge case, don't use it
      seq = [seq[i+1] - seq[i] for i in range(0, len(seq)-1)]
      _seqs.append(seq)

    _seq_last = [seq[-1] for seq in reversed(_seqs)]
    _next_val = sum(_seq_last)

    # NOTE: find which line messed up
    if any([s != 0 for s in seq]):
      print('line', i)
      print('!!!!!!!!!!', seq)
      break
    _.append(_next_val)

    # print(f'{i+1}, {len(_seqs)-2}, {_next_val}')

    # for seq in _seqs: print(seq)
    # print(_seq_last)

  r = sum(_)
  print(r)


def part2():
  _ = []
  for i in range(len(lns)):
    _seqs = []
    seq = list(map(int, lns[i].split(' ')))
    _seqs.append(seq)
    seq = [seq[i+1] - seq[i] for i in range(0, len(seq)-1)]
    _seqs.append(seq)
    while not all([s == 0 for s in seq]):
    # while sum(seq) != 0: # NOTE: has edge case, don't use it
      seq = [seq[i+1] - seq[i] for i in range(0, len(seq)-1)]
      _seqs.append(seq)

    _seq_head_with_fix = [_seqs[i][0]*(-1)**i  for i in range(len(_seqs))]
    
    _next_val = sum(_seq_head_with_fix)
    _.append(_next_val)

  r = sum(_)
  print(r)



part1()
# part2()