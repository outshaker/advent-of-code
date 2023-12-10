from functools import reduce


# f = open('d6-sample.txt',encoding='utf8')
f = open('d6.txt',encoding='utf8') # github

lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

_, rest = lns[0].split(':')
times = rest.split(' ')
times = list(map(int, filter(None, times)))
_, rest = lns[1].split(':')
distences = rest.split(' ')
distences = list(map(int, filter(None, distences)))
print(times, distences)

def f(time, distence):
  return sum([1 if i*(time-i) >= distence else 0 for i in range(2, time)])

  # v = [1 if i*(time-i) >= distence else 0 for i in range(2, time)]

  # v = []
  # for i in range(2, time):
    # if i*(time-i) > distence:
      # print(f'{i}x{time-i} > {distence}')
      # v.append(1)

  # return sum(v)

p = list(zip(times, distences))
n = len(times)
c = [f(*p[i]) for i in range(n)]
print(c)

# r = reduce(lambda acc, v: acc * v, c, 1)
# print(r)

from math import sqrt, floor, ceil

_, rest = lns[0].split(':')
time = int(rest.replace(' ', ''))
_, rest = lns[1].split(':')
distence = int(rest.replace(' ', ''))
print(time, distence)

k = time
d = distence
D = sqrt(k*k-4*d)
x_a = ceil((k-D)/2)
x_b = floor((k+D)/2)
print(D, x_a, x_b, x_b-x_a+1)

