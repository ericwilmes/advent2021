input1 = open('input1.txt', 'r')
lines = input1.readlines()

### PART 1 ###

previous = 100000000

greaterThanCounter = 0

for line in lines:
    if previous < int(line):
        greaterThanCounter += 1

    previous = int(line)

print("Part 1 answer:", greaterThanCounter)

### PART 2 ###

sums = []

count = 0

# add sums to list
for line in lines:
    if count == 0:
        prev1 = int(line)
        count += 1
    elif count == 1:
        prev2 = int(line)
        count += 1
    elif count == 2:
        sums.append(prev1+prev2+int(line))
        prev1 = prev2
        prev2 = int(line)

count = 0
previous = 9999999999

# calculate greater or lesser
for sum in sums:
    if previous < sum:
        count += 1
    previous = sum

print('Part 2 answer:', count)