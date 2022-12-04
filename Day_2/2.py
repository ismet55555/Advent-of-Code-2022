print('\n-------------------------------------------\n')
print('                   DAY X')
print('\n-------------------------------------------\n')

INPUT_FILE="input_sample.txt"
with open(INPUT_FILE, 'r') as open_file:
    input_data = open_file.readlines()
input_data = [ row.strip('\n').split(' ') for row in input_data ]

##############################################################################

print('\n===================  PART 1  ======================\n')
# A/X: Rock     - 1 - beats Scissors
# B/Y: Paper    - 2 - beats Rock
# C/Z: Scissors - 3 - beats Paper
hand_convertion = {
        "X":"A",
        "Y":"B",
        "Z":"C"
        }
win_rules = {
        "A": "C",
        "B": "A",
        "C": "B"
        }
score_map = {
        "A": 1,
        "B": 2,
        "C": 3
        }
mapping = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS"
        }

score = 0

for round_hand in input_data:
    round_hand[1] = hand_convertion[round_hand[1]]

    opponent_hand = round_hand[0]
    my_hand = round_hand[1]

    for rule_my_hand, rule_win_hand in win_rules.items():
        if my_hand == rule_my_hand and opponent_hand == rule_win_hand:
            score += 6 + score_map[my_hand]
            print(f"[Score Total: {score:3.0f}] WIN:  OP: {mapping[opponent_hand]} < YOU: {mapping[my_hand]}")
            break
        elif my_hand == opponent_hand:
            score += 3 + score_map[my_hand]
            print(f"[Score Total: {score:3.0f}] DRAW: OP: {mapping[my_hand]} = YOU: {mapping[opponent_hand]}")
            break
        elif my_hand == rule_my_hand and opponent_hand != rule_win_hand:
            score += 0 + score_map[my_hand]
            print(f"[Score Total: {score:3.0f}] LOSE: OP: {mapping[opponent_hand]} > YOU: {mapping[my_hand]}")
            break

print(f'TOTAL SCORE: {score}')


print('\n===================  PART 2  ======================\n')
outcome_rules = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
        }
# Figure out what shape to get outcome

