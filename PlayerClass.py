from DiceClass import *
from CardsClass import *
from UnitClass import *
from UnitsPrepare import selectUnits
from typing import List


class Player:
    def __init__(self, cards: List[List[int]], unitList: List[Unit], dice: List[str]):
        self.faction = unitList[0].faction
        self.handCards = cards[0]
        self.restCards = cards[1]
        self.unitList = unitList
        self.dice = dice
        self.playedCardList = []
        self.playedCard = []
        self.turnedCard = None
        self.bolterTokens = 0
        self.shieldTokens = 0
        self.bolter = dice.count('Bolter')
        self.shield = dice.count('Shield')
        self.morale = dice.count('Morale') + sum(unit.morale for unit in unitList if not unit.routed)

    def playCard(self, playedCard):
        self.turnedCard = self.handCards[playedCard]
        self.handCards.pop(playedCard)
    def turnCard(self):
        self.playedCardList.append(self.turnedCard)
        self.turnedCard = None

    def askWhatToPlay(self):
        sizeOfHand = len(self.handCards)
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
    def addRandomDie(self, amount: int = 1):
            for _ in range(amount):
                if len(self.dice) < 8:
                    self.dice.append(rollDice())
            self.dice.sort(key=sortDie)
    def recount(self):
        self.bolter = (self.dice.count('Bolter') +
                       sum(cardParameters(self.faction, card).get('Bolter') for card in self.playedCardList) +
                       self.bolterTokens)
        self.shield = (self.dice.count('Shield') +
                       sum(cardParameters(self.faction, card).get('Shield') for card in self.playedCardList) +
                       self.shieldTokens)
        self.morale = (self.dice.count('Morale') +
                       sum(cardParameters(self.faction, card).get('Morale') for card in self.playedCardList) +
                       sum(unit.morale for unit in self.unitList if not unit.routed))

    def reRollDie(self, whatDie: str, amount: int = 1):
        for _ in range(amount):
            if whatDie in self.dice:
                self.dice.remove(whatDie)
                self.dice.append(rollDice())
        self.dice.sort(key=sortDie)

    def reRollAllDie(self):
        diceCount = len(self.dice)
        self.dice = []
        self.addRandomDie(diceCount)
        self.dice.sort(key=sortDie)

    def addReinforce(self, amount: int = 1):
        for _ in range(amount):
            ifSpace = self.unitList[0].space
            self.unitList.append(Unit(self.faction,0,False,ifSpace))

class PlayerInfo:
    def __init__(self, factionList: List[int], unlockedCardList: List[bool], unitList: List[Unit]):
        player1CardList, player2CardList = selectCards(unlockedCardList)
        player1UnitList, player2UnitList = selectUnits(factionList, unitList)
        player1Dice, player2Dice = selectDice(player1UnitList, player2UnitList)
        self.player1 = Player(player1CardList, player1UnitList, player1Dice)
        self.player2 = Player(player2CardList, player2UnitList, player2Dice)
