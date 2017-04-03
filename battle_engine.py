import random
import items
import scenes

class BattleEngine(object):

	def turn(self, charA, charB):

		action_point = 1
		charA.temporary_armor = 0
	
		while action_point == 1:
	
			if not charA.playable:
				choice = self.automated()
			else:
				print(self.HP_display(charA))
				print("1. Attack \t2. Defend\n3. Item \t4. Run\n")
				choice = input(">").lower()
		
			if choice == "attack":
				if charA.weapon == None:
					print("No weapon!")
				else:
					charA.weapon.shoot(charB)
					action_point -= 1
					
			elif choice == "defend":
				print("%s takes a defensive stance." % charA.name)
				charA.temporary_armor += 2
				print("%s's defense is now %d.\n" % (charA.name, charA.temporary_armor))
				action_point -= 1
				
			elif choice == "item":
				items.print_inventory(charA)
				print("Which item do you want to use?")
				choice = input("> ")
				for item in charA.inventory:
					if choice.title() == charA.inventory[item].name:
						charA.inventory[item].use(charA)
						del charA.inventory[item]
						break
				
			elif choice == "run":
				print("%s flees from the battle." % charA.name)
				action_point -= 1
				exit(1)
	
		
	
	def battle(self, charA, charB, current_location):

		# decide who has initiative
	
		if charA.speed > charB.speed:
			first_to_go = charA
			second_to_go = charB
		else:
			first_to_go = charB
			second_to_go = charA

		print("%s goes first." % first_to_go.name)
	
		turn_count = 0
		
		# battle turn rotation
	
		while charA.alive and charB.alive:
	
			# first to go
			if charA.current_HP <= charA.max_HP / 2 and charB.current_HP <= charB.max_HP / 2:
				print(current_location.mid_battle)
			elif turn_count == 5:
				if hasattr(current_location, 'mid_battle'):
					print(current_location.mid_battle)
			
		
			print("%s's turn.\n" % first_to_go.name)
		
			self.turn(first_to_go, second_to_go)
			
			# second to go
			if not second_to_go.alive:
				break
			else:
				print("%s's turn." % second_to_go.name)
		
				self.turn(second_to_go, first_to_go)
				
			turn_count += 1

	def automated(self):
		choices = ["attack", "defend"]
		return choices[random.randint(0, len(choices) - 1)]
	
	def HP_display(self, char):
		return "■" * char.current_HP + "□" * (char.max_HP - char.current_HP) + "\n"