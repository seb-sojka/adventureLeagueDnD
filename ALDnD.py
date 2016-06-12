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
playerRace = "Variant Human"
playerClass = "Fighter"
with open("Races.csv") as csvRace:
    reader = csv.DictReader(csvRace)
    dataRaces = {}
    for row in reader:
        for header, value in row.items():
            try:
                dataRaces[header].append(value)
            except KeyError:
                dataRaces[header]=[value]
with open("Abilities.csv") as csvRace:
    reader = csv.DictReader(csvRace)
    dataAbilities = {}
    for row in reader:
        for header, value in row.items():
            try:
                dataAbilities[header].append(value)
            except KeyError:
                dataAbilities[header]=[value]
abilityCount = len(dataRaces)
raceCount = len(dataRaces['Race'])
raceNumber = dataRaces['Race'].index(playerRace)
strScore= strScore+int(dataRaces['Strength'][raceNumber])
conScore= conScore+int(dataRaces['Consitution'][raceNumber])
dexScore= dexScore+int(dataRaces['Dexterity'][raceNumber])
intScore= intScore+int(dataRaces['Intelligence'][raceNumber])
wisScore = wisScore+int(dataRaces['Wisdom'][raceNumber])
chaScore = chaScore +int(dataRaces['Charisma'][raceNumber])
conMod = int((conScore-10)/2)
chaMod = int((chaScore-10)/2)
dexMod = int((dexScore-10)/2)
intMod = int((intScore-10)/2)
wisMod = int((wisScore-10)/2)
strMod = int((wisScore-10)/2)
languages = []
languages.append(dataRaces['Language'][raceNumber])
abilities = []
count = 0
for i in range(10,abilityCount):
    count = count + 1
    if dataRaces["Ability " + str(count)][raceNumber] =='':
        break
    abilities.append(dataRaces["Ability " + str(count)][raceNumber])       
abilitiesDescription = []