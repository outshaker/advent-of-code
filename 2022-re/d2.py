f = open('d2-sample.txt',encoding='utf8')
# f = open('d2.txt',encoding='utf8')
full = f.read()
f.close()

def part1():
  def compute(s):
    if s == 'A X': return 4 # same
    elif s == 'B X': return 1 # OK
    elif s == 'C X': return 7
    elif s == 'A Y': return 8 # OK
    elif s == 'B Y': return 5 # same
    elif s == 'C Y': return 2
    elif s == 'A Z': return 3
    elif s == 'B Z': return 9
    elif s == 'C Z': return 6  # same OK

    print(sum(map(compute, full.split('\n'))))

def part2():
  def compute(s):
    if s == 'A X': return 3
    elif s == 'B X': return 1
    elif s == 'C X': return 2
    elif s == 'A Y': return 4
    elif s == 'B Y': return 5
    elif s == 'C Y': return 6
    elif s == 'A Z': return 8
    elif s == 'B Z': return 9
    elif s == 'C Z': return 7

    print(sum(map(compute, full.split('\n'))))

part1() # except 15
part2() # except 12

