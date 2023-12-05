from PlayerClass import PlayerInfo
from CardsClass import cardAction


def playTheGame(playerInfo: PlayerInfo):

    def resolveCard(round, activePlayer, playedCard, secondPlayer):
        activePlayer.turnCard()
        activePlayer.recount()
        cardAction(round, activePlayer, secondPlayer, playedCard)
        activePlayer.recount()

    def roundOperations(round, player, enemy):
        displayInfo(round, player, enemy)
        playerCard = player.askWhatToDo()
        displayInfo(round, enemy, player)
        enemyCard = enemy.askWhatToDo()
        player.playCard(playerCard)
        enemy.playCard(enemyCard)
        resolveCard(round, player, playerCard, enemy)
        resolveCard(round, enemy, enemyCard, player)

    for gameRound in range(0, 3):
        roundOperations(gameRound, playerInfo.player1, playerInfo.player2)

# Placebo function that will trow the data to the agent
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
