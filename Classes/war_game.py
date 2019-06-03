import random
"""class Enemy:
	health = 3
	def attack(self):
		print("Attack!")
		self.health -= 1
	def is_alive(self):
		if(self.health <= 0):
			print("Death!")
		else:
			print(str(self.health) + " health remaining")

enemy1 = Enemy()

enemy2 = Enemy()

print("\nEnemy1 information:")
enemy1.attack()
enemy1.attack()
enemy1.is_alive()

print("\nEnemy2 information:")
enemy2.attack()
enemy2.attack()
enemy2.attack()
enemy2.is_alive()"""


"""print("\nLETS BEGIN.........\n")

enemy1=Enemy("Osman",50000,1000,100)
enemy2=Enemy("Enemy",1000,100,10)
enemy3=Enemy()

enemy1.print()
print("\n")
enemy2.print()
print("\n")
enemy3.print()
"""

class Enemy:
	
	def __init__(self, name = "Enemy", health = 500,attack_power = 50, number_of_rounds = 10):######## Eger init yapici fonksiyonu kullanacaksak degiskenlerimizi
		self.name= name### Burada olduklari gibi self. seklinde yani class a ait bir nesnenin degiskeni
		self.health = health### Herhangi bir degisken degil gibi tanitmamiz gerek. Aksi halde class a ait bir degisken
		self.attack_power = attack_power## gibi taninmiyor python tarafindan..
		self.number_of_rounds = number_of_rounds
	
	def attack(self):
		print(self.name + "is attacking.")
		used_rounds = random.randrange(0,3)
		print(str(used_rounds) + "round used")
		self.number_of_rounds -= used_rounds

		return(used_rounds,self.attack_power)
	
	def under_attack(self, number_of_hit, attack_power):
		print(self.name + " are under attack!!!")
		self.health -= number_of_hit * attack_power

	def is_have_rounds(self):
		if self.number_of_rounds <= 0:
			print(self.name + "is speak: I haven't ammo. I Leave...")
			return True
		return False
	
	def is_alive(self):
		if self.health <= 0:
			print(self.name + "is dead!")
	
	def print(self):
		print("\nName: {}\nRemaining Health: {}\nAttack Power: {}\nNumber of Rounds: {}".format(self.name,self.health,self.attack_power,self.number_of_rounds))
	

enemies=[]

for i in range(0,10):
	health=random.randrange(100,1000)
	attack_power=random.randrange(50,500)
	number_of_rounds=random.randrange(10,100)
	enemy=Enemy("Enemy{}".format(i+1),health,attack_power,number_of_rounds)
	enemies.append(enemy)

for i in range(0,3):
	enemy_on_attack=random.randrange(0,10)
	enemy_under_attack=random.randrange(0,10)
	while enemy_under_attack == enemy_on_attack:
		enemy_under_attack=random.randrange(0,10)
	ammo_and_attack_power = enemies[enemy_on_attack].attack()
	
	enemies[enemy_under_attack].under_attack(ammo_and_attack_power[0],ammo_and_attack_power[1])

	print("\n...Round Over...\n")
	print("\nAttacked Enemy Status:\nName: {}\nRemaining Health: {}\nRemaining Rounds: {}\n".format(enemies[enemy_on_attack].name,enemies[enemy_on_attack].health,enemies[enemy_on_attack].number_of_rounds))
	print("\nUnder Attacked Enemy Status:\nName: {}\nRemaining Health: {}\nRemaining Rounds: {}\n".format(enemies[enemy_under_attack].name,enemies[enemy_under_attack].health,enemies[enemy_under_attack].number_of_rounds))
