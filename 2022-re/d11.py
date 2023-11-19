# f = open('d11-sample.txt',encoding='utf8')
f = open('d11',encoding='utf8') # github
# f = open('d11.txt',encoding='utf8')
full_text = f.read()
f.close()

import re
from operator import add, mul
from heapq import nlargest
from math import gcd



pattern = re.compile(r"^Monkey\s+(?P<no>\d+):\n\s*Starting\s+items:\s+(?P<items>(\d+,\s+)*\d+)\n\s*Operation:\s+new\s+=\s+old (?P<op>[\+\*])\s+(?P<od>\w+)\n\s*Test:\s+divisible\s+by\s+(?P<div_by>\d+)\n\s*If\strue:\sthrow\sto\smonkey\s(?P<true_to>\d+)\n\s*If\sfalse:\sthrow\sto\smonkey\s(?P<false_to>\d+)", re.MULTILINE)

# pattern = re.compile(r'''^Monkey\s+(?P<no>\d+):\n\s*
  # Starting\s+items:\s+(?P<items>(\d+,\s+)*\d+)\n\s*
  # Operation:\s+new\s+=\s+old (?P<op>[\+\*])\s+(?P<od>\w+)\n\s*
  # Test:\s+divisible\s+by\s+(?P<div_by>\d+)\n\s*
  # If\strue:\sthrow\sto\smonkey\s(?P<true_to>\d+)\n\s*
  # If\sfalse:\sthrow\sto\smonkey\s(?P<false_to>\d+)\n\s*
# , re.MULTILINE | re.VERBOSE)
# FIXME raw data with doc string

matches = list(pattern.finditer(full_text)) # => dict
# matches = pattern.findall(full_text) # => tuple
monkey_n = len(matches)
# print('monkey_n', monkey_n)

monkeys = {}

def genFunc(op, od):
  if op == '*': op_func = mul
  elif op == '+': op_func = add
  
  if od == 'old':
    if op == '*': return lambda x: mul(x, x)
    elif op == '+': return lambda x: add(x, x)
  else:
    if op == '*': return lambda x: mul(x, int(od))
    elif op == '+': return lambda x: add(x, int(od))



for match in matches:
  monkeys[int(match.group("no"))] = {
    'items': list(map(int, match.group("items").split(', '))),
    'update': genFunc(match.group("op"), match.group("od")),
    'div_by': int(match.group("div_by")),
    'true_to': int(match.group("true_to")),
    'false_to': int(match.group("false_to"))
  }

mod_by = 1
lcm = lambda a, b: abs(a * b) // gcd(a, b)
for i in range(monkey_n): mod_by = lcm(mod_by, monkeys[i]["div_by"])
print(mod_by)

# round_n = 20
# round_n = 1000
# round_n = 2000
# round_n = 3000
# round_n = 4000
# round_n = 5000
# round_n = 6000
# round_n = 7000
# round_n = 8000
# round_n = 9000
round_n = 10000
inspected_times = [0] * monkey_n

for round in range(round_n):
  for i in range(monkey_n):
    items = monkeys[i]['items']
    inspected_times[i] += len(monkeys[i]['items']) # add times

    for worry_level in items:
      update = monkeys[i]['update']
      new_worry_level = update(worry_level) // 3 # part1
      new_worry_level = update(worry_level) % mod_by # part2

      if new_worry_level % monkeys[i]['div_by'] == 0:
        next = monkeys[i]['true_to']
      else:
        next = monkeys[i]['false_to']
      # print(worry_level, new_worry_level, 'to', next)
      monkeys[next]['items'].append(new_worry_level)
      monkeys[i]['items'] = []

  # for i in range(monkey_n):
    # print('monkey',i, monkeys[i]['items'])

print(inspected_times)

no1, no2 = nlargest(2, inspected_times)
print(no1, no2, no1 * no2)

