print('part 1')

with open('Advent-3-2022-Input.txt', 'r', encoding="utf-8") as f:

    total_items_value = 0

    lines = f.readlines()

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    line_counter = 0
    counted_line_counter = 0

    for line in lines:
        line_counter += 1
        if line.strip() == "":
            print('current line empty')
        else:
            line = line.strip()
            total_number_of_items = len(line)
            compartment_size = int(total_number_of_items/2)
            misplaced_item = ''
            misplaced_item_value = 0

            first_compartment = line[0:compartment_size]
            second_compartment = line[-compartment_size:]

            for item in first_compartment:
                misplaced_item_counter = 0
                if item in second_compartment and misplaced_item_counter == 0:
                    misplaced_item = item
                    misplaced_item_counter += 1

            if misplaced_item != '':
                misplaced_item_value = letters.find(misplaced_item) + 1
                total_items_value += misplaced_item_value
                counted_line_counter += 1

print(counted_line_counter)
print(total_items_value)

print('==================================================================')
print('part 2')

with open('Advent-3-2022-Input.txt', 'r', encoding="utf-8") as f:

    all_elves_rucksack = []

    lines = f.readlines()

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for line in lines:
        if line.strip() == "":
            print('current line empty')
        else:
            line = line.strip()
            all_elves_rucksack.append(line)

all_elf_groups = []
all_elf_groups = [all_elves_rucksack[x:x+3] for x in range(0, len(all_elves_rucksack), 3)]

total_badge_value = 0

for group in all_elf_groups:
    group_badge = ''
    group_badge_value = 0
    for item in group[0]:
        if item in group[1] and item in group[2]:
            group_badge = item
    if group_badge != '':
        group_badge_value = letters.find(group_badge) + 1
        total_badge_value += group_badge_value


print(total_badge_value)