f = open("input_day1", 'r')

nums = f.readlines()
nums = [int(i) for i in nums]

for n in nums:
  for m in nums:
    if int(n)+int(m) == 2020:
      print("%s + %s = 2020" % (n, m))
      print("%s * %s = %i" % (n, m, int(n)*int(m)))

for n in nums:
  for m in nums:
    for i in nums:
      if int(n)+int(m)+int(i) == 2020:
        print("%s + %s + %s = 2020" % (n, m, i))
        print("%s * %s * %s = %i" % (n, m,i, int(n)*int(m)))
