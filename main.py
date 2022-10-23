import random, os, time

def rollDice(side):
	result = random.randint(1,side)
	return result

def health():
	healthStat = ((rollDice(6)*rollDice(12))/2)+10
	return healthStat

def strength():
	strengthStat = ((rollDice(6)*rollDice(8))/2)+12
	return strengthStat

print("CHARACTER BUILDER")
print()
c1type = input("Character Type: (Human, Elf, Wizard, Orc): ")
c1name = input("Enter your character name here: ")
print()
print("NAME:",c1name)
print("TYPE:",c1type)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("May the Great", c1name, "go down in history...")

print ("Battle Time")
c2type = input("Character Type: (Human, Elf, Wizard, Orc): ")
c2name = input("Enter your character name here: ")
print()
print("NAME:", c2name)
print("TYPE:", c2type)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()
print("May the Great", c2name, "go down in legends...")
print()

round = 1
winner = None

while True:
		time.sleep(3)
		os.system("clear")
		print("Battle Time")
		print()
		print("The battle begins!")

		c1Dice = rollDice(6)
		c2Dice = rollDice(6)

		difference = abs(c1Strength - c2Strength) + 1

		if c1Dice > c2Dice:
			c2Health -= difference
			if round == 1:
				print(c1name, "wins the first blow")
			else:
				print(c1name, "wins round", round)
		elif c2Dice > c1Dice:
			c1Health -= difference
			if round == 1:
				print(c2name, "wins the first blow")
			else:
				print(c2name, "wins round", round)
		else:
			print("Their fighting styles are a match in round" ,round, "!")
		
		print()
		print(c1name)
		print("HEALTH:", c1Health)
		print()
		print(c2name)
		print("HEALTH:", c2Health)
		print()

		if c1Health <= 0:
			print(c1name, "has lost!")
			winner = c2name
			break
		elif c2Health <= 0:
			print(c2name, "has lost!")
			winner = c1name
			break
		else:
			print("And they're both still standing for the next round!")
			round += 1

time.sleep(3)
os.system("clear")
print("BATTLE RESULTS")
print()
print(winner, "has won in", round, "rounds")
		
