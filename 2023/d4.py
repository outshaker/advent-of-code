# f = open('d4-sample.txt',encoding='utf8')
f = open('d4.txt',encoding='utf8') # github
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

def point(ln)->int:
  _, rest = ln.split(': ')
  _wn, _n = rest.split(' | ')
  wns = set(_wn.split(' ')) - {''}
  ns = set(_n.split(' ')) - {''}
  match_n = len(wns & ns)

  return 2 ** (match_n - 1) if match_n else 0

# r = sum([point(ln) for ln in lns])
# print(r)

def match(ln)->int:
  _, rest = ln.split(': ')
  _wn, _n = rest.split(' | ')
  wns = set(_wn.split(' ')) - {''}
  ns = set(_n.split(' ')) - {''}
  
  return len(wns & ns)

# modify _all
def get_copy(_all, base_n, start_i, match_n):
  for i in range(start_i + 1, start_i + 1 + match_n):
    _all[i] += base_n

_len = len(lns)
_all = [1 for i in range(_len)]
# print('_all', _all)
for i in range(_len):
  match_n = match(lns[i])
  if match_n:
    # print(f'game {i}, match_n={match_n}')
    get_copy(_all, _all[i], i, match_n)
    # print('_all', _all)
print(sum(_all))
