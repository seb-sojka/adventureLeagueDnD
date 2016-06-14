#Leads user to create a level 1 character for adventurer league play
import csv
#import Tkinter
abilityScores = [8,10,12,13,14,15]#The value for ablity scores that are possible
conScore = abilityScores[0]
strScore = abilityScores[1]
dexScore = abilityScores[2]
intScore = abilityScores[3]
wisScore = abilityScores[4]
chaScore = abilityScores[5]
playerRace = "Lightfoot Halfing"
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
with open("classes.csv") as csvRace:
    reader = csv.DictReader(csvRace)
    dataClasses = {}
    for row in reader:
        for header, value in row.items():
            try:
                dataClasses[header].append(value)
            except KeyError:
                dataClasses[header]=[value]
raceAbilityCount = len(dataRaces)
classAbilityCount = len(dataClasses)
raceCount = len(dataRaces['Race'])
raceNumber = dataRaces['Race'].index(playerRace)
classNumber = dataClasses['Class'].index(playerClass)
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
hitDie = dataClasses['Hit Die'][classNumber]
languages = []
languages.append(dataRaces['Language'][raceNumber])
abilities = []
count = 1
for i in range(10,raceAbilityCount):
    if dataRaces["Ability " + str(count)][raceNumber] =='':
        break
    abilities.append(dataRaces["Ability " + str(count)][raceNumber])       
    count = count + 1
count = 1
for i in range(9,classAbilityCount):
    if dataClasses["Ability " + str(count)][classNumber] =='':
        break
    abilities.append(dataClasses["Ability " + str(count)][classNumber])       
    count = count + 1
abilitiesLongDescription = []
abilitiesShortDescription = []
for i in range(0,len(abilities)):
    abilityNumber = dataAbilities['Ability'].index(abilities[i])
    abilitiesShortDescription.append(dataAbilities["Short Description"][abilityNumber])
    abilitiesLongDescription.append(dataAbilities["Long Description"][abilityNumber])
