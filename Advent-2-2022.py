
totalScore = 0

# Reading all lines of the file

def checkPlayedScore(playedShape):
    match playedShape:
        case 'X':
            return 1 #I play rock
        case 'Y':
            return 2 #I play paper
        case 'Z':
            return 3 #I play scissors

with open('Advent-2-2022-Input.txt', 'r', encoding="utf-8") as f:

    lines = f.readlines()

    for line in lines:
        if line.strip() == "":
            print('current line empty')
        else:
            roundScore = 0
            # Check what shape is played
            playedShape = line[2]
            print(playedShape)
            roundScore += checkPlayedScore(playedShape) 
            # Check if round is won, tied or lost
            opponentShape = line[0]
            print(opponentShape)
            match opponentShape:
                case 'A': #they play rock
                    if checkPlayedScore(playedShape) == 1: #I play rock
                        roundScore += 3
                    elif checkPlayedScore(playedShape) == 2: #I play paper
                        roundScore += 6
                    elif checkPlayedScore(playedShape) == 3: #I play scissors
                        roundScore += 0
                case 'B': #they play paper
                    if checkPlayedScore(playedShape) == 1: #I play rock
                        roundScore += 0
                    elif checkPlayedScore(playedShape) == 2: #I play paper
                        roundScore += 3
                    elif checkPlayedScore(playedShape) == 3: #I play scissors
                        roundScore += 6
                case 'C': #they play scissors
                    if checkPlayedScore(playedShape) == 1: #I play rock
                        roundScore += 6
                    elif checkPlayedScore(playedShape) == 2: #I play paper
                        roundScore += 0
                    elif checkPlayedScore(playedShape) == 3: #I play scissors
                        roundScore += 3
            print(roundScore)
            totalScore += roundScore
            print('======')

print(totalScore)

print('===========================================')
#part 2
totalScoreRound2 = 0
def checkPlayedScoreRound2(playedShape):
    match playedShape:
        case 'X':
            return 0 #I must lose
        case 'Y':
            return 3 #I must draw
        case 'Z':
            return 6 #I must win

with open('Advent-2-2022-Input.txt', 'r', encoding="utf-8") as f:

    lines = f.readlines()

    for line in lines:
        if line.strip() == "":
            print('current line empty')
        else:
            roundScore = 0
            # Check what shape is played
            playedShape = line[2]
            roundScore += checkPlayedScoreRound2(playedShape) 
            # Check if round is won, tied or lost
            opponentShape = line[0]
            match opponentShape:
                case 'A': #they play rock
                    if checkPlayedScoreRound2(playedShape) == 0: #I must lose
                        roundScore += 3 # I play scissors
                    elif checkPlayedScoreRound2(playedShape) == 6: #I must win
                        roundScore += 2 # I play paper
                    elif checkPlayedScoreRound2(playedShape) == 3: #I must draw
                        roundScore += 1 # I play rock
                case 'B': #they play paper
                    if checkPlayedScoreRound2(playedShape) == 0: #I must lose
                        roundScore += 1 # I play rock
                    elif checkPlayedScoreRound2(playedShape) == 6: #I must win
                        roundScore += 3 # I play scissors
                    elif checkPlayedScoreRound2(playedShape) == 3:#I must draw
                        roundScore += 2 # I play paper
                case 'C': #they play scissors
                    if checkPlayedScoreRound2(playedShape) == 0: #I must lose
                        roundScore += 2 # I play paper
                    elif checkPlayedScoreRound2(playedShape) == 6: #I must win
                        roundScore += 1 # I play rock
                    elif checkPlayedScoreRound2(playedShape) == 3: #I must draw
                        roundScore += 3 # I play scissors
            totalScoreRound2 += roundScore

print(totalScoreRound2)


