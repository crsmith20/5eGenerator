# -*- coding: utf-8 -*-
"""
Character Class
"""

class Character:
    
    def __init__(self, race, lvlClass, align, bGround):
        self.__race = race
        self.__class = lvlClass
        self.__align = align
        self.__bGround = bGround
        
    def getRace(self):
        return self.__race
    
    def getClass(self):
        return self.__class
    
    def getBackground(self):
        return self.__bGround
    
    def getAlign(self):
        return self.__align
    
    def toString(self):
        return "A " + self.__align + ", " + self.__bGround + ", " + self.__race + " " + self.__class
    
def genRace(x):
        races = ["Arakoocra", "Aasimar", "Bugbear", "Dragonborn", "Dwarf", "Elf", "Firbolg", "Genasi", "Gnome", "Goblin", "Goliath",
                 "Half-Elf", "Halfling", "Half-Orc", "Hobgoblin", "Human", "Kenku", "Kobold", "Lizardfolk", "Orc", "Tabaxi", "Tiefling",
                 "Tortle", "Triton", "Yuan-ti Pureblood"]
        x = x % len(races)
        return races[x]
        
def genClass(x):
        classes = ["Barbarian", "Bard", "Druid", "Monk", "Paladin", "Ranger", "Sorcerer", "Warlock"]
        x = x % len(classes)
        return classes[x]
        
def genAlign(x):
        alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral",
                      "Lawful Evil", "Neutral Evil", "Chaotic Neutral"]
        x = x % len(alignments)
        return alignments[x]
    
def genBackground(x):
        backgrounds = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit", "Noble",
                       "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]
        x = x % len(backgrounds)
        return backgrounds[x]
    

    
    