file = open("ReactorReports.txt", "r")
reports = file.read()
reports = reports.split('\n')


def test(direction, lst, position):
    if direction == "increasing":
        if position < len(lst)-1:
            if int(lst[position + 1]) > int(lst[position]) and int(lst[position+1]) - int(lst[position]) <= 3:
                return test("increasing", lst, position+1)
            else:
                return False
    else:
        if position < len(lst)-1:
            if int(lst[position + 1]) < int(lst[position]) and int(lst[position]) - int(lst[position+1]) <= 3:
                return test("decreasing", lst, position+1)
            else:
                return False
    return True


total = 0

for item in reports:
    safe = False
    item = item.split(" ")
    if int(item[1]) > int(item[0]):
        safe = test("increasing", item, 0)
    elif int(item[1]) < int(item[0]):
        safe = test("decreasing", item, 0)
    if safe:
        total += 1

print(total)
