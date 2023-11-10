from copy import deepcopy
from functools import reduce
import re

# f = open('d5-sample.txt',encoding='utf8')
f = open('d5.txt',encoding='utf8')
fullText = f.read()
f.close()

head, tail = fullText.split('\n\n')
head = head.split('\n')
tail = tail.split('\n')

# 3 1 3 1 3 1 3 1 3 ...
# 3, 7, 11, ..., n*4-1=L
# n=(L+1)//4
# 1 5 9 ... no*4-3=i
# no=(i+3)//4

getN = lambda L: (L+1)//4
N = getN(len(head[0]))
print(N)

qus = [[] for i in range(N)]
for n in range(len(head)):
    for i in range(1, len(head[n]), 4):
        if 'A' <= head[n][i] <= 'Z':
            no = (i+3)//4
            # print(no, head[n][i])
            qus[no-1].append(head[n][i])
        # elif head[n][i] == ' ':
            # print('-')
        # else:
            # print(head[n][i])

stks = list(map(lambda q: list(reversed(q)), qus))
# print(qus, stks)

# ---

# TODO 處理 'move {n} from {src} to {dest}'
# s = 'move 1 from 2 to 1'
# pat = r'move (\d+) from (\d+) to (\d+)'
# m = re.compile(pat)
# result = m.match(s)
# print(result.groups())

def part1(stks):
  def move(stks, n, src, dest):
    for i in range(n):
      stks[dest].append(stks[src].pop())

  pat = r'move (\d+) from (\d+) to (\d+)'
  m = re.compile(pat)
  for n in range(len(tail)):
    result = m.match(tail[n])
    n, src, dest = list(map(int, result.groups()))
    # print(n, src, dest)
    move(stks, int(n), int(src)-1, int(dest)-1)
    # print(stks)

  print(reduce(lambda c,i: c+i, map(lambda s: s[-1], stks)))

def part2(stks):
  def move(stks, n, src, dest):
    x = stks[src][-n:]
    stks[src][-n:] = []
    stks[dest].extend(x)

  pat = r'move (\d+) from (\d+) to (\d+)'
  m = re.compile(pat)
  for n in range(len(tail)):
      result = m.match(tail[n])
      n, src, dest = list(map(int, result.groups()))
      # print(n, src, dest)
      move(stks, int(n), int(src)-1, int(dest)-1)
      # print(stks)

  print(reduce(lambda c,i: c+i, map(lambda s: s[-1], stks)))

part1(deepcopy(stks))
part2(deepcopy(stks))
