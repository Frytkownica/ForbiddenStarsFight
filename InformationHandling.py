
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