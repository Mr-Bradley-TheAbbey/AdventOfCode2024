l = open("locationIDs.txt", "r")
file = l.read()
file = file.split('\n')
left = []
right = []
for location in file:
    left.append(location[0:5])
    right.append(location[8:14])
left.sort()
right.sort()

total = 0
for item in left:
    noOfTimes = 0
    for other in right:
        if item == other:
            noOfTimes += 1
    total += int(item) * noOfTimes

print(total)



