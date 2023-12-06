def cardParameters(faction: int, cardNumber: int):
    mapping = {
        0: {
            # Reconnaissance
            0: {'Bolter': 0, 'Shield': 1, 'Morale': 0},
            # Faith in the Emperor
            1: {'Bolter': 0, 'Shield': 0, 'Morale': 1},
            # Ambush
            2: {'Bolter': 1, 'Shield': 0, 'Morale': 0},
            # Fury of the Ultramar
            3: {'Bolter': 1, 'Shield': 0, 'Morale': 0},
            # Blessed Power armour
            4: {'Bolter': 0, 'Shield': 1, 'Morale': 0},
            # Hold the line
            5: {'Bolter': 0, 'Shield': 1, 'Morale': 1},
            # Glory and death
            6: {'Bolter': 1, 'Shield': 0, 'Morale': 1},
            # Veteran scouts
            7: {'Bolter': 1, 'Shield': 1, 'Morale': 1},
            # Drop Pod assault
            8: {'Bolter': 1, 'Shield': 1, 'Morale': 0},
            # Show no fear
            9: {'Bolter': 0, 'Shield': 2, 'Morale': 1},
            # Break the line
            10: {'Bolter': 1, 'Shield': 2, 'Morale': 0},
            # Armoured advance
            11: {'Bolter': 2, 'Shield': 1, 'Morale': 0},
            # Emperor's glory
            12: {'Bolter': 0, 'Shield': 2, 'Morale': 2},
            # Emperor's might
            13: {'Bolter': 3, 'Shield': 0, 'Morale': 0}
        },
        1: {
            # Slugga Boyz
            0: {'Bolter': 1, 'Shield': 1, 'Morale': 0},
            # Shoota Boyz
            1: {'Bolter': 2, 'Shield': 0, 'Morale': 0},
            # 'Ard Boyz
            2: {'Bolter': 0, 'Shield': 2, 'Morale': 0},
            # Gretchin
            3: {'Bolter': 0, 'Shield': 0, 'Morale': 0},
            # Mek Boyz
            4: {'Bolter': 0, 'Shield': 0, 'Morale': 1},
            # Biker Nobz
            5: {'Bolter': 2, 'Shield': 1, 'Morale': 0},
            # Sea of green
            6: {'Bolter': 1, 'Shield': 1, 'Morale': 0},
            # Waaagh!!!!
            7: {'Bolter': 0, 'Shield': 0, 'Morale': 3},
            # Mega Nobz
            8: {'Bolter': 1, 'Shield': 2, 'Morale': 0},
            # Rokkit wagon
            9: {'Bolter': 3, 'Shield': 0, 'Morale': 0},
            # Weirdboyz
            10: {'Bolter': 1, 'Shield': 1, 'Morale': 1},
            # Party wagon
            11: {'Bolter': 1, 'Shield': 2, 'Morale': 0},
            # Snapper Gargant
            12: {'Bolter': 4, 'Shield': 1, 'Morale': 0},
            # Smasher Gargant
            13: {'Bolter': 2, 'Shield': 3, 'Morale': 0}
        }
    }
    return mapping.get(faction, {}).get(cardNumber, {})