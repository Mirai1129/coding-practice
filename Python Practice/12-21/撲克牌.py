import random
points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
kinds = ['S', 'H', 'D', 'C']
cards = []


def poker():
    for i in kinds:
        for j in points:
            card = i + j
            cards.append(card)
    random.shuffle(cards)  # 洗牌
    target_cards = random.choices(cards, k=10)
    players = [random.choices(cards, k=5), random.choices(
        cards, k=5), random.choices(cards, k=5), random.choices(cards, k=5)]
    score = [0, 0, 0, 0]
    for i in range(0, 5):
        if players[0][i] in target_cards:
            score[0] += 1
        if players[1][i] in target_cards:
            score[1] += 1
        if players[2][i] in target_cards:
            score[2] += 1
        if players[3][i] in target_cards:
            score[3] += 1
    print("{}\n\n{}\n\n{}\n\n{}".format(cards, target_cards, players, score))
    print("winner is player", score.index(max(score))+1)


poker()
