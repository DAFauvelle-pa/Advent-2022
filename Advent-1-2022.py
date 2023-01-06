class Elf:

    def __init__(self):

        self.caloryTotal = 0

        self.caloryList = []

    def calculateTotalCalory(self):
        for i in self.caloryList:
            self.caloryTotal += i

# List of elves

allElves = []

# Reading all lines of the file

with open('Advent-1-2022-Input.txt', 'r', encoding="utf-8") as f:

    currentElf = Elf()

    lines = f.readlines()

    for line in lines:
        if line.strip() == "":
            allElves.append(currentElf)
            nextElf = Elf()
            currentElf = nextElf
        else:
            currentElf.caloryList.append(int(line))

# Check how many elves

print(len(allElves))

# Check highest kcal count

highestCal = 0
for elf in allElves:
    elf.calculateTotalCalory()
    if elf.caloryTotal >= highestCal:
        highestCal = elf.caloryTotal

print(highestCal)

# Check top three kcal carrying elves

calTotalAll = []


for elf in allElves:
    calTotalAll.append(elf.caloryTotal)
    calTotalAll.sort(reverse=True)

print(len(calTotalAll))
top3TotalCal = 0

for i in range(3):
    top3TotalCal += calTotalAll[i]

print(top3TotalCal)
