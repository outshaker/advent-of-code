# f = open('d3-sample.txt',encoding='utf8')
f = open('d3.txt',encoding='utf8') # github
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

isSymbol = lambda c: c in "~`!@#$%^&*()_+-={}[]|\;:,/<>?"
isNum = lambda c: c in "1234567890"
getXY = lambda x, y: lns[y][x]

w, h = len(lns[0]), len(lns)

def get_nums_syms(ln):
  in_num = False
  num = ''
  start = 0
  nums = []
  syms = []
  for i in range(len(ln)):
    c = ln[i]
    if isSymbol(c):
      syms.append((c, i))
      if in_num == True: # is tail
        in_num = False
        nums.append((num, start, i-1))
        num = ''
        start = 0
    elif isNum(c):
      if in_num == False: # is head
        start = i
        in_num = True
      num += c # append num
    else:
      if in_num == True: # is tail
        in_num = False
        nums.append((num, start, i-1))
        num = ''
        start = 0

  return nums, syms

def hasSymbol(num, syms): # sym at same line
  a, z = num[1]-1, num[2]+1
  for sym in syms:
    if a == sym[1] or sym[1] == z: return sym[0]
  return None

def hasSymbol2(num, syms): # sym at next line
  a, z = num[1]-1, num[2]+1
  for sym in syms:
    if a <= sym[1] <= z: return sym[0]
  return None

def hasNum(sym, nums): # nums at same line
  for num in nums:
    if num[2] == sym[1]: return num[0]
    elif num[1] == sym[1]: return num[0]
  return None

def hasNum2(sym, nums): # nums at next line
  for num in nums:
    if num[2] == sym[1]: return num[0]
    elif num[1] == sym[1]: return num[0]
    elif num[1] <= sym[1] <= num[2]: return num[0]
  return None

matches = []
# next_nums, next_syms = None, None
nums, syms = [None] * h, [None] * h
for j in range(h):
  # print('line', j)
  # this_nums, this_syms = get_nums_syms(lns[j])
  # next_nums, next_syms = get_nums_syms(lns[j+1])

  # if len(this_nums):
    # for num in this_nums:
      # sym = hasSymbol(num, this_syms)
      # if sym:
        # print(f'{num} match {sym}')
        # matches.append(int(num[0]))
      # sym = hasSymbol2(num, next_syms)
      # if sym:
        # print(f'{num} match {sym}')
        # matches.append(int(num[0]))

  # if len(this_syms):
    # for sym in this_syms:
      # num = hasNum(sym, this_nums)
      # if num:
        # print(f'{sym} match {num}')
        # matches.append(int(num))
      # num = hasNum2(sym, next_nums)
      # if num:
        # print(f'{sym} match {num}')
        # matches.append(int(num))

  nums[j], syms[j] = get_nums_syms(lns[j])

# print(nums)
# print(syms)



# check nums in line
for j in range(h):
  ns = nums[j]
  # print('line', j)
  for n in ns:
    if j > 0 and hasSymbol2(n, syms[j-1]): # sym at pre line
      matches.append(int(n[0]))
      # print(n[0], end=' ')
      continue
    if hasSymbol(n, syms[j]): # sym at same line
      matches.append(int(n[0]))
      # print(n[0], end=' ')
      continue
    if j < h-1 and hasSymbol2(n, syms[j+1]): # sym at next line
      matches.append(int(n[0]))
      # print(n[0], end=' ')
      continue
  print('')

# print(nums, syms)
print(matches, sum(matches))
# print(sum(matches))








