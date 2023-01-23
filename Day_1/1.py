print('\n-------------------------------------------\n')
print('                   DAY 1')
print('\n-------------------------------------------\n')

INPUT_FILE="input.txt"
with open(INPUT_FILE, 'r') as open_file:
    input_data = open_file.readlines()
input_data = [ row.strip('\n') for row in input_data ]

##############################################################################

print('\n===================  PART 1  ======================\n')
elf_calorie_totals = [0]
for item in input_data:
    if not item:
        elf_calorie_totals.extend([0])
        continue
    elf_calorie_totals[-1] += int(item)
    
print('Elf max calories:')
print(max(elf_calorie_totals))


print('\n===================  PART 2  ======================\n')
elf_calorie_top = sorted(elf_calorie_totals)

print('Top 3 calorie totals:')
print(sum(elf_calorie_top[-3:]))


