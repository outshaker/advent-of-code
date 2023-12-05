f = open('d5-sample.txt',encoding='utf8')
# f = open('d5.txt',encoding='utf8') # github

full_text = f.read()
f.close()


def part1():
  parts = full_text.split('\n\n')
  # print(parts)

  _, rest = parts[0].split(': ')
  seeds = list(map(int, rest.split(' ')))
  print('seeds', seeds)

  def m(seed, _maps):
    for _map in _maps:
      start, end, fix = _map
      if start <= seed <= end:
        # print(f'seed#{seed} in ({start}, {end}), seed = {seed} + {fix}')
        return seed + fix # x => y = x + fix

    # print(f'no match, seed = {seed}')
    return seed # x => y = x

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
  _ranges = list(map(toRange, chunks))
  _ranges.sort(key=lambda x: x[0])
  print('ranges', _ranges)

  def is_overlap(r1, r2):
    d1 = r1[1]-r1[0]
    d2 = r2[1]-r2[0]
    _ = (r1[0],r1[1],r2[0],r2[1])
    return d1+d2 > max(_)-min(_)

  def get_overlap(r1, r2):
    _ = sorted([r1[0],r1[1],r2[0],r2[1]])
    return (_[1], _[2])

  def m(seed, _maps):
    for _map in _maps:
      start, end, fix = _map
      if start <= seed <= end:
        # print(f'seed#{seed} in ({start}, {end}), seed = {seed} + {fix}')
        return seed + fix # x => y = x + fix

    # print(f'no match, seed = {seed}')
    return seed # x => y = x


  _next_ranges = []

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
  for _map in _maps: print(f'{_map[0]}-{_map[1]}', end=' ')
  print('')

  for _range in _ranges:
    # print('_range', _range)
    for _map in _maps:
      r1 = (_map[0], _map[1])
      # print('_map', r1)
      # 計算 _map 中跟 _range 重疊的部分，計算出最小值
      # _map => 小切片

      if is_overlap(r1, _range):
        # print('is_overlap')
        overlap = get_overlap(r1, _range)
        # print('overlap', overlap)
        _next_range = (m(overlap[0], _maps), m(overlap[1], _maps))
        _next_ranges.append(_next_range)
        # print(_next_ranges)
        print(overlap, '=>', _next_range)
      # else:
        # print('not is_overlap')

  _ranges = _next_ranges
  _next_ranges = []
  # for part in parts[2:3]: # map 2
  for part in parts[2:]: # map 2 to map n
    _, rest = part.split(':\n')
    pairs = rest.split('\n')
    pairs = list(map(lambda x: map(int, x.split(' ')), pairs))
    _maps = []
    for pair in pairs:
      y0, x0, n = pair
      fix = y0 - x0
      # print(f'when x in ({x0},{x0+n-1}), f(x)= x+({fix})')
      _maps.append((x0,x0+n-1,fix))
    
    _maps.sort(key=lambda x: x[0])
    for _map in _maps: print(f'{_map[0]}-{_map[1]}', end=' ')
    print('')
  
    for _range in _ranges:
      # print('_range', _range)
      for _map in _maps:
        r1 = (_map[0], _map[1])
        # print('_map', r1)
        # 計算 _map 中跟 _range 重疊的部分，計算出最小值
        # _map => 小切片

        if is_overlap(r1, _range):
          # print('is_overlap')
          overlap = get_overlap(r1, _range)
          # print('overlap', overlap)
          _next_range = (m(overlap[0], _maps), m(overlap[1], _maps))
          _next_ranges.append(_next_range)
          # print(_next_ranges)
          print(overlap, '=>', _next_range)
        # else:
          # print('not is_overlap')

  # NOTE: final ranges is location
  _next_ranges.sort(key=lambda x: x[0])
  print(_next_ranges)
  rlst = list(map(lambda _range: _range[0], _next_ranges))
  print(rlst)
  r = min(rlst)
  print(r)

# part1()
part2()
