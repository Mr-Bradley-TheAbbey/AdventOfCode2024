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
for i in range(len(left)):
    total += (abs(int(left[i]) - int(right[i])))

print(total)