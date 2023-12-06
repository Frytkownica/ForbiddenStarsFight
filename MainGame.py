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

