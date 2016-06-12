#Leads user to create a level 1 character for adventurer league play
import csv
import numpy as np
#import Tkinter
abilityScores = [8,10,12,13,14,15]#The value for ablity scores that are possible
conScore = abilityScores[0]
strScore = abilityScores[1]
dexScore = abilityScores[2]
intScore = abilityScores[3]
wisScore = abilityScores[4]
chaScore = abilityScores[5]
playerRace = "Normal Human"
playerClass = "Fighter"
with open("Races.csv") as csvRace:
    reader = csv.DictReader(csvRace)
    data ={}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header]=[value]
raceNumber = data['Race'].index(playerRace)
strScore= strScore+int(data['Strength'][raceNumber])
conScore= conScore+int(data['Consitution'][raceNumber])
dexScore= dexScore+int(data['Dexterity'][raceNumber])
intScore= intScore+int(data['Intelligence'][raceNumber])
wisScore = wisScore+int(data['Wisdom'][raceNumber])
chaScore = chaScore +int(data['Charisma'][raceNumber])
conMod = int((conScore-10)/2)