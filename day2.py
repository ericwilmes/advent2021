input2 = open("input2.txt", "r")
lines = input2.readlines()

depth = 0
position = 0

for line in lines:
    command, amount = line.split(" ")
    amount = int(amount)
    if command == "forward":
        position += amount
    elif command == "down":
        depth += amount
    elif command == "up":
        depth -= amount

print("Part 1 answer:", depth*position)

depth = 0
position = 0
aim = 0

for line in lines:
    command, amount = line.split(" ")
    amount = int(amount)
    if command == "forward":
        position += amount
        depth += (aim*amount)
    elif command == "down":
        aim += amount
    elif command == "up":
        aim -= amount

print("Part 2 answer:", depth*position)