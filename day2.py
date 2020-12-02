f = open("input_day2", 'r')

counter = 0

for line in f:
  times, character, password = line.split(" ", 2)
  min_appearance, max_appearance = times.split("-", 1)
  character = character[:-1]
  password = password.rstrip("\n")
  if int(min_appearance) <= password.count(character) <= int(max_appearance):
    counter += 1
print("Number of validated passwords: %s" % (counter))


f = open("input_day2", 'r')

counter = 0

for line in f:
  times, character, password = line.split(" ", 2)
  pos1, pos2 = times.split("-", 1)
  character = character[:-1]
  password = password.rstrip("\n")
  if (password[int(pos1)-1] is character) ^ (password[int(pos2)-1] is character):
    counter += 1
print("Number of validated passwords: %s" % (counter))
