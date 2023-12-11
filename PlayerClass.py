from DiceClass import *
from UnitClass import *
from CardsIcons import cardParameters
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
        self.cardPlayedThisRound = None
        self.bolterTokens = 0
        self.shieldTokens = 0
        self.bolter = dice.count('Bolter')
        self.shield = dice.count('Shield')
        self.morale = dice.count('Morale') + sum(unit.morale for unit in unitList if not unit.routed)

    def turnCard(self):
        if self.cardPlayedThisRound is not None:
            self.playedCardList.append(self.cardPlayedThisRound)
            self.cardPlayedThisRound = None
        self.recount()

    def askWhatToPlay(self):
        sizeOfHand = len(self.handCards) - 1
        while True:
            try:
                selectedCard = int(input(f"Play card between 0 and {sizeOfHand}: "))
                if 0 <= selectedCard <= sizeOfHand:
                    break
                else:
                    print("Number out of range. Please try again.")
            except ValueError:
                print(f"Invalid input. Play card between 0 and {sizeOfHand}: ")
        self.cardPlayedThisRound = self.handCards[selectedCard]
        self.handCards.pop(selectedCard)
        return self.cardPlayedThisRound

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

    def dealDamage(self, damage: int):
        damage -= self.shield
        while damage > 0:
            print(f"Damage to deal {damage}")
            unitList = [unit for unit in self.unitList if unit.routed is False]
            unroutedUnits = len(unitList)
            match unroutedUnits:
                case 0:
                    unroutedUnits = len(self.unitList)
                    match unroutedUnits:
                        case 0:
                            damage = 0
                        case 1:
                            damage = self.dealDamageToNUnit(damage)
                        case default:
                            unitDeltDemage = int(input(f"Select unit to route 0 to {unroutedUnits - 1}"))
                            if 0 <= unitDeltDemage < unroutedUnits - 1:
                                damage = self.dealDamageToNUnit(damage, unitDeltDemage)
                case 1:
                    damage = self.dealDamageToNUnroutedUnit(damage)
                case default:
                    try:
                        unitDeltDemage = int(input(f"Select unit to route 0 to {unroutedUnits - 1}"))
                        if 0 <= unitDeltDemage < unroutedUnits - 1:
                            damage = self.dealDamageToNUnroutedUnit(damage,unitDeltDemage)
                        else:
                            print("Number out of range. Please try again.")
                    except ValueError:
                            print(f"Invalid input. Enter a number between 0 and {unroutedUnits - 1}:")
    def dealDamageToNUnroutedUnit(self, damage: int, number: int=0):
        count = -1
        for unroutedUnitN, unit in enumerate(self.unitList):
            if unit.routed is False:
                count += 1
                if count == number:
                    return self.dealDamageToNUnit(damage, unroutedUnitN)

    def dealDamageToNUnit(self, damage: int, number: int=0):
        if damage < self.unitList[number].hp:
            self.unitList[number].routed = True
            return 0
        else:
            damage -= self.unitList[number].hp
            self.unitList.pop(number)
            return damage

    def flushAfterRound(self):
        self.bolterTokens = 0
        self.shieldTokens = 0
        self.recount()


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
            self.unitList.append(Unit(self.faction, 0, False, ifSpace))


class PlayerInfo:
    def __init__(self, factionList: List[int], unlockedCardList: List[bool], unitList: List[Unit]):
        player1CardList, player2CardList = self.selectCards(unlockedCardList)
        player1UnitList, player2UnitList = selectUnits(factionList, unitList)
        player1Dice, player2Dice = selectDice(player1UnitList, player2UnitList)
        self.player1 = Player(player1CardList, player1UnitList, player1Dice)
        self.player2 = Player(player2CardList, player2UnitList, player2Dice)

    def selectCards(self, unlockedcardList: List[bool]):
        if len(unlockedcardList) != 28:
            raise ValueError("unlockedcardList must have 28 elements.")

        def selectRange(startIndex: int):
            return [unlockedcardList[element] for element in range(startIndex, startIndex + 14)]

        def selectPlayerCards(rangedList: List[int]):
            availableTypes = [cardNumber for cardNumber in range(14) if rangedList[cardNumber]]
            # Making doublets
            selectionPool = [cardNumber for cardNumber in availableTypes for _ in range(2)]
            # Shuffle Deck
            random.shuffle(selectionPool)
            selectedCards = selectionPool[0:5]
            remainingCards = selectionPool[5:10]
            return selectedCards, remainingCards

        player1Cards = selectPlayerCards(selectRange(0))
        player2Cards = selectPlayerCards(selectRange(14))

        return player1Cards, player2Cards
