#Leads user to create a level 1 character for adventurer league play
import csv

global dataRaces
dataRaces = {}
global dataAbilities
dataAbilities = {}
global dataClasses
dataClasses = {}

def printShortDescriptions(abilities):#Prints a short descriptions of the abilities based on race and class
    print
    for i in range(0,len(abilities)):
        abilityNumber = dataAbilities['Ability'].index(abilities[i])
        print("%s : %s" %(abilities[i], dataAbilities["Short Description"][abilityNumber]))
        print
    
def openCSV(): #Opens the csv and places the infomation into lists
    with open("Races.csv") as csvRace:
        reader = csv.DictReader(csvRace)
        for row in reader:
            for header, value in row.items():
                try:
                    dataRaces[header].append(value)
                except KeyError:
                    dataRaces[header]=[value]
    with open("Abilities.csv") as csvRace:
        reader = csv.DictReader(csvRace)
        for row in reader:
            for header, value in row.items():
                try:
                    dataAbilities[header].append(value)
                except KeyError:
                    dataAbilities[header]=[value]
    with open("classes.csv") as csvRace:
        reader = csv.DictReader(csvRace)
        for row in reader:
            for header, value in row.items():
                try:
                    dataClasses[header].append(value)
                except KeyError:
                    dataClasses[header]=[value]
scorePlacement = ['Strength', 'Dexterity', 'Consitution', 'Intelligence', 'Wisdom', 'Charisma']

availableScores = [8,10,12,13,14,15]#The value for ablity scores that are possible
abilityScores = availableScores

openCSV()#Gets infomation from the CSV

raceAbilityCount = len(dataRaces)
classAbilityCount = len(dataClasses)

for index in range(len(dataRaces['Race'])): #Displays the possible races
    print index + 1, ' ', dataRaces['Race'][index]
raceNumber = input("Please ener the number with your race choice: ") -1 #Prompts user to enter number related to thier race choice

abilities = []
count = 1

for i in range(10,raceAbilityCount): #Gather abilities gain from race choice
    if dataRaces["Ability " + str(count)][raceNumber] =='':
        break
    abilities.append(dataRaces["Ability " + str(count)][raceNumber])       
    count = count + 1
printShortDescriptions(abilities)#Prints short descriptions of abilities from player's race

for index in range(len(dataClasses['Class'])): #Displays the possible classes
    print index + 1, ' ', dataClasses['Class'][index]
classNumber = input("Please ener the number with your race choice: ") -1 #Prompts user to enter thier class choice number base

count = 1
for i in range(9,classAbilityCount):
    if dataClasses["Ability " + str(count)][classNumber] =='':
        break
    abilities.append(dataClasses["Ability " + str(count)][classNumber])       
    count = count + 1
    
printShortDescriptions(abilities)
print abilityScores
for i in range (0,len(abilityScores)):
    abilityScores[i] = int(dataRaces[scorePlacement[i]][raceNumber])+abilityScores[i] 
print abilityScores
hitDie = dataClasses['Hit Die'][classNumber]
languages = []
languages.append(dataRaces['Language'][raceNumber])

for i in range(0,len(abilities)):#Prints long description of players abilities based on race and class 
    abilityNumber = dataAbilities['Ability'].index(abilities[i])
    print("%s : %s" %(abilities[i], dataAbilities["Long Description"][abilityNumber]))
    print
print ("Languages: %s and Common" % languages[0])
