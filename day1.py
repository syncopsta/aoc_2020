f = open("input_day1", 'r')

nums = f.readlines()
nums = [int(i) for i in nums]

for n in nums:
  for m in nums:
    if n+m == 2020:
      print("%s + %s = 2020" % (n, m))
      print("%s * %s = %i" % (n, m, n*m))
      break
  else:
    continue
  break
for n in nums:
  for m in nums:
    for i in nums:
      if n+m+i == 2020:
        print("%s + %s + %s = 2020" % (n, m, i))
        print("%s * %s * %s = %i" % (n, m,i, n*m*i))
        break
    else:
      continue
    break
