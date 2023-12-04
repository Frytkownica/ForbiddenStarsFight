from PlayerClass import PlayerInfo


def playTheGame(playerInfo: PlayerInfo):
    def askWhatToDo(player):
        sizeOfHand = len(player.handCards)
        while True:
            try:
                selectedCard = int(input(f"Enter a number between 1 and {sizeOfHand}: "))
                if 1 <= selectedCard <= sizeOfHand:
                    break
                else:
                    print("Number out of range. Please try again.")
            except ValueError:
                print(f"Invalid input. Enter a number between 1 and {sizeOfHand}: ")
        return selectedCard - 1

    def playCard(player, playedCard):
        player.playedCard.append(player.handCards[playedCard])
        player.handCards.pop(playedCard)

    def resolveCard(player, playedCard, enemy):
        player.playedCardList.append(player.playedCard)
        player.turnedCard=[]
        player.recount
        cardAction(player, enemy, playedCard)
        player.recount

    def roundOperations(round, player, enemy):
        displayInfo(round, player, enemy)
        playerCard = askWhatToDo(player)
        displayInfo(round, enemy, player)
        enemyCard = askWhatToDo(enemy)
        playCard(player, playerCard)
        playCard(enemy, enemyCard)
        resolveCard(round, player, playerCard, enemy)
        resolveCard(round, enemy, enemyCard, player)

    for round in range(0, 3):
        roundOperations(round, playerInfo.player1, playerInfo.player2)


def displayInfo(round, player, enemy):
    print("Round ", round)
    print("Hand ", player.handCards)
    print("Unit You ")
    for unit in player.unitList:
        unit.toString()
    print("Unit Enemy")
    for unit in enemy.unitList:
        unit.toString()
    print("Faction ", player.faction)
    print("Dice You", player.dice)
    print("Dice Enemy", enemy.dice)
    print("Cards Played", player.playedCardList)
    print("Cards Enemy", enemy.playedCardList)
    print(f"Stats You B:{player.bolter} S:{player.shield} M:{player.morale}")
    print(f"Stats Enemy B:{enemy.bolter} S:{enemy.shield} M:{enemy.morale}")
