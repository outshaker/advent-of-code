f = open('d7-sample.txt',encoding='utf8')
# f = open('d7',encoding='utf8') # github
# f = open('d7.txt',encoding='utf8')
lns = f.readlines()
lns = list(map(str.strip, lns)) # 去除結尾換行
f.close()

# ls => add dir
# cd => check path is avaible, switch path

# cd / => ['']
# cd x => [].append(x)
# cd .. => [].pop()
# [] tostr => '/'.join([])

# / a => ['', a]
# / d => ['', d]
# / a / e => ['', a, e]


# get cd path => new_path_list, path_str
def cd_path(path, d):
  path_to_str = lambda path: '/'.join(path) or '/'

  if d == '/': return [''], '/'
  elif d == '..':
    new_path_list = path.copy()
    new_path_list.pop()
    return new_path_list, path_to_str(new_path_list)
  else:
    new_path_list = path.copy()
    new_path_list.append(d)
    return new_path_list, path_to_str(new_path_list)


path, path_str = [], ''
ls_flag = False

path_size_nodir = {}
has_sub_dir =set()
path_size = {}

for ln in lns:
  if ln.startswith('$ cd'):
    if ls_flag: ls_flag = False # turn off ls_flag

    _, cmd, d = ln.split()
    path, path_str = cd_path(path, d)
    # print('cd to ', path_str)

  elif ln.startswith('$ ls'):
    ls_flag = True # turn on ls_flag
    path_size_nodir[path_str] = 0

  else: # list file size, file name
    if not ls_flag: # error case
      print('list file but ls_flag is off')
    else:
      if ls_flag and not ln.startswith('dir'): # file
        sz, n = ln.split()
        path_size_nodir[path_str] += int(sz)
      else: # dir
        has_sub_dir.add(path_str)

# print(path_size_nodir)
# for path, sz in path_size_nodir.items():
  # print(path, sz)

# print(has_sub_dir)
all_dir_paths = list(path_size_nodir.keys())
for path in all_dir_paths:
  # if path == '/': # ignore root dir
    # pass
  if path in has_sub_dir:
    path_with_sub_dir = list(filter(lambda p: p.startswith(path), all_dir_paths))
    # print(path, list(path_with_sub_dir))
    path_size[path] = sum(map(lambda k: path_size_nodir[k], path_with_sub_dir))
  elif not path in has_sub_dir:
    path_size[path] = path_size_nodir[path]

# print(path_size)
# for path, sz in path_size.items():
  # if sz <= 100000: print(path, sz)

r = sum(filter(lambda sz: sz <= 100000, path_size.values()))
print(f'part1={r}') # part1: except 95437

total_space = 70000000
except_free_space = 30000000
used_space = sum(path_size_nodir.values()) # except 48381165
print(f'used_space={used_space}') # 44795677
min_clean_up_space = except_free_space - (total_space - used_space) # except 8381165
print(f'min_clean_up_space={min_clean_up_space}') # 4795677

r2 = min(filter(lambda sz: sz >= min_clean_up_space, path_size.values()))
print(f'part2={r2}') # part2: except 24933642
