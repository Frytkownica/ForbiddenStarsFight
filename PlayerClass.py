from DiceClass import selectDice
from CardsClass import *
from UnitClass import *
from UnitsPrepare import selectUnits
from typing import List
class Player:
    def __init__(self, cards:List[int], unitList:List[Unit], dice:List[str]):
        self.faction = unitList[0].faction
        self.handCards = cards[0]
        self.restCards = cards[1]
        self.unitList = unitList
        self.dice = dice
        self.playedCardList = []
        self.playedCard = []
        self.bolterTokens = 0
        self.shieldTokens = 0
        self.bolter = dice.count('Bolter')
        self.shield = dice.count('Shield')
        self.morale = dice.count('Morale') + sum(unit.morale for unit in unitList if not unit.routed)

    def recount(self):
        self.bolter = (dice.count('Bolter') +
                       sum(cardParameters(self.faction, card).get('Bolter') for card in self.playedCardList) +
                       self.bolterTokens)
        self.shield = (dice.count('Shield') +
                       sum(cardParameters(self.faction, card).get('Shield') for card in self.playedCardList) +
                       self.shieldTokens)
        self.morale = (dice.count('Morale') +
                       sum(cardParameters(self.faction, card).get('Morale') for card in self.playedCardList) +
                       sum(unit.morale for unit in unitList if not unit.routed))


class PlayerInfo:
    def __init__(self, factionList: List[int], unlockedCardList: List[bool], unitList: List[Unit]):
        player1CardList, player2CardList = selectCards(unlockedCardList)
        player1UnitList, player2UnitList = selectUnits(factionList, unitList)
        player1Dice, player2Dice = selectDice(player1UnitList, player2UnitList)
        self.player1 = Player(player1CardList, player1UnitList, player1Dice)
        self.player2 = Player(player2CardList, player2UnitList, player2Dice)
