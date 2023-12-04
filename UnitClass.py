class Unit:
    def __init__(self, faction: int, CL: int, routed: bool, space: bool):
        unitInfoRead = UnitInfo(faction, CL, space)
        #print(unitInfoRead)
        self.faction = faction
        self.cl = CL
        self.routed = routed
        self.space = space
        self.dice = unitInfoRead.get('dice')
        self.hp = unitInfoRead.get('hp')
        self.morale = unitInfoRead.get('morale')
    def toString(self):
        #print("faction ", self.faction, end=", ")
        print("CL ", self.cl, end=", ")
        print("Routed ", self.routed, end=", ")
        print("Space ", self.space, end=", ")
        #print("Dice", self.dice, end=", ")
        print("HP ", self.hp, end=", ")
        print("Morale ", self.morale)


def UnitInfo(faction: int, CL: int, space: bool):
    mapping = {
        # Faction Space Marines
        0: {
            False: {
                0: {'dice': 1, 'hp': 2, 'morale': 2},
                1: {'dice': 2, 'hp': 3, 'morale': 3},
                2: {'dice': 3, 'hp': 4, 'morale': 3},
                3: {'dice': 3, 'hp': 5, 'morale': 4}
            },
            True: {
                0: {'dice': 2, 'hp': 2, 'morale': 2},
                2: {'dice': 4, 'hp': 5, 'morale': 4}
            }
        },
        # Faction Orc
        1: {
            False: {
                0: {'dice': 2, 'hp': 2, 'morale': 1},
                1: {'dice': 2, 'hp': 4, 'morale': 2},
                2: {'dice': 3, 'hp': 5, 'morale': 2},
                3: {'dice': 3, 'hp': 6, 'morale': 3}
            },
            True: {
                0: {'dice': 1, 'hp': 3, 'morale': 2},
                2: {'dice': 3, 'hp': 6, 'morale': 4}
            }
        },
    }
    return mapping.get(faction,{}).get(CL, {}).get(space,{})
