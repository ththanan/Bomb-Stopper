scores = []
rankscores = []
def ranking():
    global scores, rankscores
    with open('score.txt') as file:
        for line in file:
            name, score = line.split(',')
            score = int(score)
            scores.append((name, score))
        scores.sort(key=lambda s: s[1])
        scores.reverse()
        for num in range(0, 5):
            rankscores.append(scores[num])
        file.flush()
ranking()