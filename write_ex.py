score = 0

#read current high score
with open('highscore.txt', 'r') as f:
    highscore = int(f.readline())
    
score += 7

if score > highscore:
    print('you have the high score')
    
    with open('highscore.txt', 'w') as f:
        f.write(str(score))
else:
    print('the high score was not yours')