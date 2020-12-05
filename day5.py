with open("input_day5", "r") as f:
  passes = [line.strip().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1") for line in f.readlines()]
hid = 0
for entry in passes:
  seat_id = 8 * int(entry[:-3], 2) + int(entry[-3:], 2)
  if seat_id > hid:
    hid = seat_id
print(hid)