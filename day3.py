from timeit import default_timer as timer
start = timer()

def tree_hitter(right, down):
  counter = 0
  for i, row in enumerate(grid[::down]):
    if row[i * right % horizontal] == "#":
      counter +=1
  return counter

grid = open("input_day3").read().split()
horizontal = len(grid[0])
print("The number of trees: %s" % (tree_hitter(3,1)))

counter = 1
for multiply in [tree_hitter(right, down) for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]]:
  counter *= multiply
print(counter)

end = timer()
print(end - start)