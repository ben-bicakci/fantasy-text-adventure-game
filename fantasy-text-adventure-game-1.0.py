# fantasy-text-adventure-game-1.0.py
# By Ben Bicakci
# 2019

import random
import time

weapons = {'wooden club': (5, 15), 'sword': (15, 25), 'fangs': (10, 15), 'tree trunk': (30, 50)}
items_info = ['sword (15-25 damage)', 'health potion (+ 20 health)']
items = ['sword', 'health potion']
freeitem = ''

player = {'Health': 100, 'Weapon': '', 'Damage' : '', 'Defence': 0, 'Gold': 0}
enemy = {'Health': 100, 'Weapon': '', 'Damage' : '', 'Defence': 0, 'Gold': 0}
player['Damage'] = weapons['wooden club']
player['Weapon'] = 'wooden club'

enemytype = ''
escape = ''

ok_decisions = ['fight', 'run']	#Could also add go to inventory option to heal?
decision = ''
pathchoice = ''
pathchoices = ['forest', 'home']

def enemy_gen():
	global enemytype
	global enemy
	event1 = random.randint(1,10)
	if event1 <= 4:
		enemytype = 'Giant Spider'
		enemy['Damage'] = weapons['fangs']
		enemy['Weapon'] = 'fangs'
		enemy['Health'] += 20
		enemy['Gold'] += 10
	elif event1 >= 5 and event1 <= 8:
		enemytype = 'Bandit'
		enemy['Damage'] = weapons['sword']
		enemy['Weapon'] = 'sword'
		enemy['Gold'] += 20
	else:
		enemytype = 'Ogre'
		enemy['Health'] += 100
		enemy['Damage'] = weapons['tree trunk']
		enemy['Weapon'] = 'tree trunk'
		enemy['Gold'] += 100

enemy_gen()

def combat(player, enemy):
	print()
	time.sleep(1)
	print()
	print('The ' + enemytype + ' attacks you! \n')
	time.sleep(1)
	player_damage = random.randrange(*weapons[player['Weapon']])
	enemy_damage = random.randrange(*weapons[enemy['Weapon']])
	player['Health'] -= enemy_damage
	enemy['Health'] -= player_damage
	print_pause([
	('You hit the ' + enemytype + ' for ' + str(player_damage) + ' damage!', 1),
	(enemytype + ' hits you for ' + str(enemy_damage) + ' damage!', 0.5),
	])
	print_pause([('Your health: ' + str(player['Health']), 0),
	(enemytype + "'s health: " + str(enemy['Health']), 1),
	])
	print()

def print_pause(lines):
	for line, pause in lines:
		print(line)
		time.sleep(pause)

def stats_inventory():
	print()
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('Stats: ')
	print(player)
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	time.sleep(2)
	print()

def inventory_update():
	if freeitem == 'sword':
		player['Weapon'] = freeitem
		player['Damage'] = weapons['sword']
	else:
		player['Health'] += 20

def escape_attempt():
	global escape
	global decision
	escape = random.randint(0,1)
	if escape == 0:
		print('You try to run but the ' + enemytype + ' catches you!')
		time.sleep(0.5)
		decision = 'fight'
	if escape == 1:
		print('You manage to run away from the ' + enemytype + '.')
		time.sleep(1)

def loot():
	global player
	if enemytype == 'Giant Spider':
		print('You loot 10 gold from the body')
		player['Gold'] += 10
	elif enemytype == 'Bandit':
		print('You loot 20 gold from the body')
		player['Gold'] += 20
	else:
		print('You loot 100 gold from the body')
		player['Gold'] += 100

#def level_system():
#level system place holder
	
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Welcome to Very Basic Fantasy Text Game')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
time.sleep(1)
print()

#Title screen place holder

stats_inventory()

#Still need to print conversations letter-by-letter

print_pause([
	('As you walk home along a dirt path, you come across a travelling merchant.', 2),
	('Travelling Merchant: "Hello, adventurer. What is your name?"', 1),
	])
name = input()
print_pause([
	("Travelling Merchant: Hello, " + name + ".", 2),
	("I will give you one free item to start you off on your adventure.", 3),
	('You may choose from the following:', 0),
	(items_info, 2)
	])
print()
print('Which item will you take?')
	
while freeitem.lower() not in items:
	freeitem = input('sword or health potion ?\n')
	if freeitem.lower() not in items:
		print()
		print_pause([
			("Travelling Merchant: I am but a humble merchant, I do not have that item.", 1),
			("I can only offer you one of these:", 0),
			])
else:
	print()
	print_pause([
		('Travelling Merchant: Good choice, ' + name + '.', 1),
		('I hope this ' + freeitem + ' serves you well on your adventure!', 2),
		])

#Add the selected free item to Player's inventory, update, and display stats
inventory_update()
stats_inventory()

print_pause([
	('Equipped with your new ' + freeitem + ' you set off on your way home.', 2),
	('Up ahead, the path forks off into a forest.', 2),
	('You hear a sound from the forest...', 2),
	('Do you enter the forest to investigate, or continue on home?', 2),
	])
print()
while pathchoice.lower() not in pathchoices:
	pathchoice = input('Which way will you go: forest or home?\n')
	if pathchoice.lower() == 'forest':
		print()
		time.sleep(1)
		print_pause([('You are ambushed by a ' + enemytype + '! \n', 1),
		('Player: ' + str(player) + '\n', 0),
		(enemytype + ': ' + str(enemy) + '\n', 0),
		])
		decision = input('Stay and fight or try to run? \n')
		while decision.lower() not in ok_decisions:
			decision = input('Fight or run? \n')
		while decision.lower() in ok_decisions and escape != 1:
			if decision.lower() == ok_decisions[0]:
				time.sleep(1)
				combat(player, enemy)
				if enemy['Health'] <= 0 and player['Health'] > 0:
					print()
					print('You defeated the ' + enemytype + '!')
					time.sleep(1)
					print()
					loot()
					break
				elif enemy['Health'] <= 0 and player['Health'] <= 0:
					print()
					print('You and the ' + enemytype + ' both fell in combat!')
					time.sleep(1)
					break
				elif player['Health'] <= 0 and enemy['Health'] > 0:
					print()
					print_pause([
					('The ' + enemytype + ' defeated you! \n', 1),
					])
					break
				else:
					decision = input('Stay and fight or try to run? \n')
					while decision.lower() not in ok_decisions:
						decision = input('Fight or run? \n')
			elif decision.lower() == ok_decisions[1]:
				escape_attempt()
			else:
				decision = input('Fight or run? \n')
	else:
		if pathchoice.lower() == 'home':
			print_pause([
			('You return home. \n', 1),
			])
		
stats_inventory()

restart = input('R to restart or Q to quit \n') #not implemented yet