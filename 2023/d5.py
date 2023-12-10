# map one poiont to next
def m(seed, _maps):
  for _map in _maps:
    start, end, fix = _map
    if start <= seed <= end:
      # print(f'seed#{seed} in ({start}, {end}), seed = {seed} + {fix}')
      return seed + fix # x => y = x + fix

  # print(f'no match, seed = {seed}')
  return seed # x => y = x

# map range to next
def mr(_range, _maps):
  return (m(_range[0], _maps), m(_range[1], _maps))

def is_overlap(r1, r2):
  d1 = r1[1]-r1[0]
  d2 = r2[1]-r2[0]
  _ = (r1[0],r1[1],r2[0],r2[1])
  return d1+d2 > max(_)-min(_)

def get_overlap(r1, r2):
  _ = sorted([r1[0],r1[1],r2[0],r2[1]])
  return (_[1], _[2])

avg = lambda lst: sum(lst) / len(lst)





# f = open('d5-sample.txt',encoding='utf8')
f = open('d5.txt',encoding='utf8') # github

full_text = f.read()
f.close()


def part1():
  parts = full_text.split('\n\n')
  # print(parts)

  _, rest = parts[0].split(': ')
  seeds = list(map(int, rest.split(' ')))
  print('seeds', seeds)

  # for part in parts[1:2]: # line 2
  for part in parts[1:]: # line 2 to line n
    _, rest = part.split(':\n')
    pairs = rest.split('\n')
    pairs = list(map(lambda x: map(int, x.split(' ')), pairs))
    _maps = []
    for pair in pairs:
      y0, x0, n = pair
      fix = y0 - x0
      # print(f'when x in ({x0},{x0+n-1}), f(x)= x+({fix})')
      _maps.append((x0,x0+n-1,fix))
    _maps.sort(key=lambda x: x[0]) # DD
    # print(_maps)

    mm = lambda seed: m(seed, _maps)
    seeds = list(map(mm, seeds))
    # print(seeds)
    print('---')
  # r = min(seeds)
  # print(r)


def part2():
  parts = full_text.split('\n\n')
  # print(parts)

  _, rest = parts[0].split(': ')
  seeds = list(map(int, rest.split(' ')))
  chunks = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
  toRange = lambda x: (x[0], x[0]+x[1]-1)
  segAs = list(map(toRange, chunks))
  segAs.sort(key=lambda x: x[0])
  print('segAs', segAs)
  # print('avg_rng_szs', avg([r[1]-r[0] for r in segAs]))

  _, rest = parts[1].split(':\n')
  pairs = rest.split('\n')
  pairs = list(map(lambda x: map(int, x.split(' ')), pairs))
  _maps = []
  for pair in pairs:
    y0, x0, n = pair
    fix = y0 - x0
    # print(f'when x in ({x0},{x0+n-1}), f(x)= x+({fix})')
    _maps.append((x0,x0+n-1,fix))
  _maps.sort(key=lambda x: x[0])

  # for _map in _maps: print(f'{_map[0]}~{_map[1]}')
  # print('')
  # print('avg_map_sz', avg([m[1]-m[0] for m in _maps]))

  _next_segAs = []
  for segA in segAs[0:1]: # dev
  # for segA in segAs:
    # 找出seg.start 大於 segA.start 而且有重疊的範圍段，作為候選項目，按照 start 由小到大排列，命名為範圍段C
    # 從 segA.start 開始，範圍段C 的第一個 segC[i] 做處理

    # 走訪到 segC[i].start，(segA.start, segC[i].start-1) 這段作預設 map (fix=0)
    # 走訪到 loc = min(segA.end, segC[i].end) 這段作 map (fix=segC[i].fix)
    # 當前位置設定為 loc，如果 loc == segA.end 結束處理
      # 如果還沒到，就表示應該還有範圍段C，繼續處理，起始點更新為 loc+1

    start, end = segA
    print('start, end = ', segA)
    segCs = list(filter(lambda s: is_overlap(segA, (s[0], s[1])), _maps))
    print('len(segCs)', len(segCs))
    print('segCs', segCs)

    if len(segCs) == 1: # sample case
      segC = (segCs[0][0], segCs[0][1]) # reorganize
      overlap = get_overlap(segC, segA)
      print('overlap', overlap)
      if overlap == segA: # segA is covered by segC
        print('all cover: segA is covered by segC')
        _next_segA = mr(segA, _maps)
        _next_segAs.append(_next_segA)
      elif overlap == segC: # segC is covered by segA
        print('segC is part of segA')
        print('!!!!!!!!!!!!!!!!!!!!')
        print('segA, segC', segA, segC)
        # 把 segA 截斷為三段傳入 mr() 處理，或是
      else:
        print('segA, segC', segA, segC)
        _next_segA = mr((loc, overlap[0]-1), _maps)
        _next_segAs.append(_next_segA)
        _next_segA = mr(overlap, _maps)
        _next_segAs.append(_next_segA)
    else:
      print('len(segCs) != 1')
      print('!!!!!!!!!!!!!!!')
      print('segCs', segCs)
      # for seg in segCs:

    print(segA, '=>', _next_segAs)



  # NOTE: final ranges is location
  _next_segAs.sort(key=lambda x: x[0])
  print(_next_segAs)
  rlst = list(map(lambda _range: _range[0], _next_segAs))
  print(rlst)
  r = min(rlst)
  print(r)

# part1()
part2()
