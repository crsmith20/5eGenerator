# -*- coding: utf-8 -*-
"""
@author: Chris
Main File
"""

import character
import random

def main():
    race = character.genRace(random.randint(0, 100))
    align = character.genAlign(random.randint(0, 100))
    classes = character.genClass(random.randint(0, 100))
    bGround = character.genBackground(random.randint(0, 100))

    player = character.Character(race, classes, align, bGround)
    
    print(player.toString())
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    