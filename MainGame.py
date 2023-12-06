from PlayerClass import *
from CardsActions import cardAction
from InformationHandling import displayInfo


def playTheGame(playerInfo: PlayerInfo):

    def resolveCard(round : int, activePlayer : Player, enemy : Player, playedCard : int):
        activePlayer.turnCard()
        activePlayer.recount()
        cardAction(round, activePlayer, enemy, playedCard)
        activePlayer.recount()

    def roundOperations(round, attacker, defender):
        displayInfo(round, attacker, defender)
        attackerPlayedCard = attacker.askWhatToPlay()
        displayInfo(round, defender, attacker)
        defenderPlayedCard = defender.askWhatToPlay()
        resolveCard(round, attacker, defender, attackerPlayedCard)
        resolveCard(round, defender, attacker, defenderPlayedCard)

    for gameRound in range(0, 3):
        roundOperations(gameRound, playerInfo.player1, playerInfo.player2)

