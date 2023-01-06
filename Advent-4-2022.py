print('part 1')

with open('Advent-4-2022-Input.txt', 'r', encoding="utf-8") as f:

    lines = f.readlines()

    pair_counter = 0
    pair_overlap_counter = 0

    for line in lines:
        if line.strip() == "":
            print('current line empty')
        else:
            pair_counter += 1
            #do stuff
            elf_pair = line.strip()
            both_elves = elf_pair.split(',')
            both_elves_ids = []

            for elf_range in both_elves:
                elf_range_ids = elf_range.split('-')
                both_elves_ids.append(elf_range_ids)

            if both_elves_ids[0][0] > both_elves_ids[1][0]:
                if both_elves_ids[0][1] <= both_elves_ids[1][1]:
                    pair_overlap_counter += 1

            if both_elves_ids[0][0] < both_elves_ids[1][0]:
                if both_elves_ids[0][1] >= both_elves_ids[1][1]:
                    pair_overlap_counter += 1

            if both_elves_ids[0][0] == both_elves_ids[1][0]:
                if both_elves_ids[0][1] >= both_elves_ids[1][1] or both_elves_ids[0][1] < both_elves_ids[1][1]:
                    pair_overlap_counter += 1


    print(pair_overlap_counter)
    print(pair_counter)