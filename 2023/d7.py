from collections import Counter
from functools import cmp_to_key

# f = open('d7-sample.txt',encoding='utf8')
f = open('d7.txt',encoding='utf8') # github

lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

# part1
def cmp(log, log2):
  def _cmp(v, v2):
    if v < v2: # asc
      return -1
    elif v == v2:
      return 0
    else: # desc
      return +1

  def pat_cmp(h, h2):
    pat2lv = {
      '5': 7,
      '41': 6,
      '32': 5,
      '311': 4,
      '221': 3,
      '2111': 2,
      '11111': 1
    }
    toPat = lambda h_str: ''.join(list(map(lambda t: str(t[1]), Counter(h_str).most_common())))
    plv, plv2 = pat2lv[toPat(h)], pat2lv[toPat(h2)]
    # print('pat_cmp', h, h2, plv, plv2, _cmp(plv, plv2))
    return _cmp(plv, plv2)

  def label_cmp(h, h2):
    char2lv = lambda h_char: "23456789TJQKA".find(h_char)

    for i in range(len(h)):
      clv, clv2 = char2lv(h[i]), char2lv(h2[i])
      if clv != clv2: return _cmp(clv, clv2)
    return 0

  h, h2 = log[0], log2[0]
  pat_cmp_result = pat_cmp(h, h2)
  label_cmp_result = label_cmp(h, h2)
  # print(h, h2, pat_cmp_result, label_cmp_result)

  if pat_cmp_result != 0: return pat_cmp_result

  return label_cmp(h, h2)

# part2
def cmp2(log, log2):
  def _cmp(v, v2):
    if v < v2: # asc, <
      return -1
    elif v == v2: # ==
      return 0
    else: # desc, >
      return +1

  def pat_cmp(h, h2):
    def get_pat_lv(h_str):
      pat2lv = {
        '5': 7,
        '41': 6,
        '32': 5,
        '311': 4,
        '221': 3,
        '2111': 2,
        '11111': 1
      }
      c = Counter(h_str)
      pat = ''.join(list(map(lambda t: str(t[1]), c.most_common())))
      origin_lv = pat2lv[pat]

      j_cout = c['J']
      if j_cout == 1:
        _fix = { 1:2, 2:4, 3:5, 4:6, 6:7 }
      elif j_cout == 2:
        _fix = { 2:4, 3:6, 5:7 }
      elif j_cout == 3:
        _fix = { 4:6, 5:7 }
      elif j_cout == 4:
        _fix = { 6:7 }
      else:
        _fix = {}

      if _fix.get(origin_lv): return _fix[origin_lv]
      return origin_lv

    plv, plv2 = get_pat_lv(h), get_pat_lv(h2)
    # print('pat_cmp', h, h2, plv, plv2, _cmp(plv, plv2))
    return _cmp(plv, plv2)

  def label_cmp(h, h2):
    char2lv = lambda h_char: "J23456789TQKA".find(h_char)

    for i in range(len(h)):
      clv, clv2 = char2lv(h[i]), char2lv(h2[i])
      if clv != clv2: return _cmp(clv, clv2)
    return 0

  h, h2 = log[0], log2[0]
  pat_cmp_result = pat_cmp(h, h2)
  label_cmp_result = label_cmp(h, h2)
  # print(h, h2, pat_cmp_result, label_cmp_result)

  if pat_cmp_result != 0: return pat_cmp_result

  return label_cmp(h, h2)


logs = []
pats = []
for ln in lns:
  hand, bid = ln.split(' ')
  bid = int(bid)
  logs.append((hand, bid))
# print(logs)

# logs = sorted(logs, key=cmp_to_key(cmp)) # part1
logs = sorted(logs, key=cmp_to_key(cmp2)) # part2
# print(logs)

# for i in range(len(logs)): print(f'{i+1} * {logs[i][1]}')
r_ = [(i+1) * logs[i][1] for i in range(len(logs))]
# print(r_)

r = sum(r_)
print(r)




