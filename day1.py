numbers = open('input_day1').read().split('\n')
numbers.pop()
for n in numbers:
  for m in numbers:
    if int(n)+int(m) == 2020:
      print("%s + %s = 2020" % (n, m))
      print("%s * %s = %i" % (n, m, int(n)*int(m)))


for n in numbers:
  for m in numbers:
    for i in numbers:
      if int(n)+int(m)+int(i) == 2020:
        print("%s + %s + %s = 2020" % (n, m, i))
        print("%s * %s * %s = %i" % (n, m,i, int(n)*int(m)))

