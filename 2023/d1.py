# f = open('d1-sample.txt',encoding='utf8')
# f = open('d1-sample2.txt',encoding='utf8')
f = open('d1.txt',encoding='utf8') # github
# f = open('d1.txt',encoding='utf8')
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

def f(ln):
  d = list(filter(lambda c: c in '123456789', ln))
  a, z = d[0], d[-1]
  return int(a+z)

s = sum([f(ln) for ln in lns])
print(s)

# tab = [
  # ('one', '1'),
  # ('two', '2'),
  # ('three', '3'),
  # ('four', '4'),
  # ('five', '5'),
  # ('six', '6'),
  # ('seven', '7'),
  # ('eight', '8'),
  # ('nine', '9')
# ]

# fail
# def replace_dig(ln):
  # for t in tab:
    # ln = ln.replace(t[0], t[1])
  # return ln

# s2 = sum([f(replace_dig(ln)) for ln in lns])
# print(s2)



# match o,t,f,s,e,n for number
# o => 1
# t => 2, 3
# f => 4, 5
# s => 6, 7
# e => 8
# n => 9

def find_first_n(ln: str) -> int|None:
  for i in range(len(ln)):
    c = ln[i]
    if c in "123456789":
      return c
    elif c == 'o':
      if ln[i:].startswith('one'): return '1'
    elif c == 't':
      if ln[i:].startswith('two'): return '2'
      if ln[i:].startswith('three'): return '3'
    elif c == 'f':
      if ln[i:].startswith('four'): return '4'
      if ln[i:].startswith('five'): return '5'
    elif c == 's':
      if ln[i:].startswith('six'): return '6'
      if ln[i:].startswith('seven'): return '7'
    elif c == 'e':
      if ln[i:].startswith('eight'): return '8'
    elif c == 'n':
      if ln[i:].startswith('nine'): return '9'
  return None

# e => one, three, five , nine
# o => two
# r =>four
# x => six
# n => seven
# t => eight

def find_last_n(ln: str) -> str|None:
  for i in range(len(ln)):
    c = ln[i]
    if c in "123456789":
      return c
    elif c == 'e':
      if ln[i:].startswith('eno'): return '1'
      if ln[i:].startswith('eerht'): return '3'
      if ln[i:].startswith('evif'): return '5'
      if ln[i:].startswith('enin'): return '9'
    elif c == 'o':
      if ln[i:].startswith('owt'): return '2'
    elif c == 'r':
      if ln[i:].startswith('ruof'): return '4'
    elif c == 'x':
      if ln[i:].startswith('xis'): return '6'
    elif c == 'n':
      if ln[i:].startswith('neves'): return '7'
    elif c == 't':
      if ln[i:].startswith('thgie'): return '8'
  return None

def g(ln):
  a, z = find_first_n(ln), find_last_n(ln[::-1])
  return int(a + z)

s = sum([g(ln) for ln in lns])
print(s)

