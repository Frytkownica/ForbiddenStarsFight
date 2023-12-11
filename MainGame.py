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
        attacker.dealDamage(defender.bolter)
        defender.dealDamage(attacker.bolter)
        attacker.flushAfterRound()
        defender.flushAfterRound()
    endCheck = True
    while endCheck:
        for gameRound in range(0, 3):
            roundOperations(gameRound, playerInfo.player1, playerInfo.player2)
            if gameRound == 2 or len(playerInfo.player1.unitList)*len(playerInfo.player2.unitList) == 0:
                endCheck = False



