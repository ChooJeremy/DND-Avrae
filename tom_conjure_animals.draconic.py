embed
<drac2> 
### Get arguments from avrae
args = &ARGS&

### Data
animals = {
	"blood hawk": {
		"name": "Blood Hawk",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d4",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"init_mod": 2,
		"count": 8,
		"has_adv": True,
		"Special": ""
	},
	"camel": {
		"name": "Camel",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "1d4",
			"damage_bonus": 0
		}],
		"type": "Bludgeoning",
		"init_mod": -1,
		"count": 8,
		"has_adv": False,
		"Special": ""
	},
	"flying snake": {
		"name": "Flying Snake",
		"attacks": [{
			"to_hit": 6,
			"damage_roll": "3d4",
			"damage_bonus": 1
		}],
		"type": "Poison (1 piercing)",
		"init_mod": +4,
		"count": 8,
		"has_adv": False,
		"Special": ""
	},
	"giant crab": {
		"name": "Giant Crab",
		"attacks": [{
			"to_hit": 3,
			"damage_roll": "1d6",
			"damage_bonus": 1
		}],
		"type": "Bludgeoning",
		"init_mod": 2,
		"count": 8,
		"has_adv": False,
		"Special": "Hit: the target is grappled (escape DC 11). The crab has two claws, each of which can grapple only one target."
	},
	"giant rat": {
		"name": "Giant Rat",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d4",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"init_mod": 2,
		"count": 8,
		"has_adv": True,
		"Special": ""
	},
	"giant weasel": {
		"name": "Giant Weasel",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "1d4",
			"damage_bonus": 3
		}],
		"type": "Piercing",
		"init_mod": 3,
		"count": 8,
		"has_adv": False,
		"Special": ""
	},
	"mastiff": {
		"name": "Mastiff",
		"attacks": [{
			"to_hit": 3,
			"damage_roll": "1d6",
			"damage_bonus": 1
		}],
		"type": "Piercing",
		"init_mod": 2,
		"count": 8,
		"has_adv": False,
		"Special": "Hit: If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone."
	},
	"mule": {
		"name": "Mule",
		"attacks": [{
			"to_hit": 2,
			"damage_roll": "1d4",
			"damage_bonus": 2
		}],
		"type": "Bludgeoning",
		"init_mod": 0,
		"count": 8,
		"has_adv": False,
		"Special": ""
	},
	"poisonous snake": {
		"name": "Poisonous Snake",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "0",
			"damage_bonus": 1
		}],
		"type": "Piercing",
		"init_mod": 3,
		"count": 8,
		"has_adv": False,
		"Special": "Hit: the target must make a DC 10 Constitution saving throw, taking 5 (2d4) poison damage on a failed save, or half as much damage on a successful one."
	},
	"pony": {
		"name": "Pony",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "2d4",
			"damage_bonus": 2
		}],
		"type": "Bludgeoning",
		"init_mod": 0,
		"count": 8,
		"has_adv": False,
		"Special": ""
	},
	"stirge": {
		"name": "Stirge",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "1d4",
			"damage_bonus": 3
		}],
		"type": "Piercing",
		"init_mod": 3,
		"count": 8,
		"has_adv": False,
		"Special": "Hit: the stirge attaches to the target. While attached, the stirge doesn't attack. Instead, at the start of each of the stirge's turns, the target loses 5 (1d4 + 3) hit points due to blood loss.\n\nThe stirge can detach itself by spending 5 feet of its movement. It does so after it drains 10 hit points of blood from the target or the target dies. A creature, including the target, can use its action to detach the stirge."
	},
	"axe beak": {
		"name": "Axe Beak",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d8",
			"damage_bonus": 2
		}],
		"type": "Slashing",
		"init_mod": 1,
		"count": 6,
		"has_adv": False,
		"Special": ""
	},
	"boar": {
		"name": "Boar",
		"attacks": [{
			"to_hit": 3,
			"damage_roll": "1d6",
			"damage_bonus": 1
		}],
		"type": "Slashing",
		"init_mod": 0,
		"count": 6,
		"has_adv": False,
		"Special": "Charge. If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 3 (1d6) slashing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone."
	},
	"constrictor snake": {
		"name": "Constrictor Snake",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d8",
			"damage_bonus": 2
		}],
		"type": "Bludgeoning",
		"init_mod": 2,
		"count": 6,
		"has_adv": False,
		"Special": "Hit: the target is grappled (escape DC 14). Until this grapple ends, the creature is restrained, and the snake can't constrict another target."
	},
	"draft horse": {
		"name": "Draft Horse",
		"attacks": [{
			"to_hit": 6,
			"damage_roll": "2d4",
			"damage_bonus": 4
		}],
		"type": "Bludgeoning",
		"init_mod": 0,
		"count": 6,
		"has_adv": False,
		"Special": ""
	},
	"elk": {
		"name": "Elk",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "2d4",
			"damage_bonus": 3
		}],
		"type": "Bludgeoning",
		"init_mod": 0,
		"count": 6,
		"has_adv": False,
		"Special": "Charge. If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
	},
	"giant badger": {
		"name": "Giant Badger",
		"attacks": [{
			"to_hit": 3,
			"damage_roll": "1d6",
			"damage_bonus": 1
		}, {
			"to_hit": 3,
			"damage_roll": "2d4",
			"damage_bonus": 1
		}],
		"type": "Piercing and Slashing",
		"init_mod": 0,
		"count": 6,
		"has_adv": False,
		"Special": ""
	},
	"giant bat": {
		"name": "Giant Bat",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d6",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"init_mod": 3,
		"count": 6,
		"has_adv": False,
		"Special": ""
	},
	"giant centipede": {
		"name": "Giant Centipede",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d4",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"init_mod": 2,
		"count": 6,
		"has_adv": False,
		"Special": "Hit: the target must succeed on a DC 11 Constitution saving throw or take 10 (3d6) poison damage. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
	},
	"giant frog": {
		"name": "Giant Frog",
		"attacks": [{
			"to_hit": 3,
			"damage_roll": "1d4",
			"damage_bonus": 1
		}],
		"type": "Piercing",
		"init_mod": 1,
		"count": 6,
		"has_adv": False,
		"Special": "Hit: the target is grappled (escape DC 11). Until this grapple ends, the target is restrained, and the frog can't bite another target."
	},
	"giant lizard": {
		"name": "Giant Lizard",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d8",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"init_mod": 1,
		"count": 6,
		"has_adv": False,
		"Special": ""
	},
	"giant owl": {
		"name": "Giant Owl",
		"attacks": [{
			"to_hit": 3,
			"damage_roll": "2d6",
			"damage_bonus": 1
		}],
		"type": "Piercing",
		"init_mod": 2,
		"count": 6,
		"has_adv": False,
		"Special": ""
	},
	"giant poisonous snake": {
		"name": "Giant Poisonous Snake",
		"attacks": [{
			"to_hit": 6,
			"damage_roll": "1d4",
			"damage_bonus": 4
		}],
		"type": "Piercing",
		"init_mod": 4,
		"count": 6,
		"has_adv": False,
		"Special": "Hit: the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one."
	},
	"giant wolf spider": {
		"name": "Giant Wolf Spider",
		"attacks": [{
			"to_hit": 3,
			"damage_roll": "1d6",
			"damage_bonus": 1
		}],
		"type": "Piercing",
		"init_mod": 3,
		"count": 6,
		"has_adv": False,
		"Special": "Hit: the target must make a DC 11 Constitution saving throw, taking 7 (2d6) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
	},
	"panther": {
		"name": "Panther",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d6",
			"damage_bonus": 2
		}],
		"type": "Piercing or Slashing",
		"init_mod": 2,
		"count": 6,
		"has_adv": False,
		"Special": "Pounce. If the panther moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. If the target is prone, the panther can make one bite attack against it as a bonus action. Note: If clawing, reducing damage by number of hits + crits (claws roll 1d4 instead of 1d6)"
	},
	"riding horse": {
		"name": "Riding Horse",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "2d4",
			"damage_bonus": 3
		}],
		"type": "Bludgeoning",
		"init_mod": 0,
		"count": 6,
		"has_adv": False,
		"Special": ""
	},
	"wolf": {
		"name": "Wolf",
		"name_plural": "Wolves",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "2d4",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"init_mod": 2,
		"count": 6,
		"has_adv": True,
		"Special": "Hit: if the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone."
	},
	"ape": {
		"name": "Ape",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "1d6",
			"damage_bonus": 3
		}, {
			"to_hit": 5,
			"damage_roll": "1d6",
			"damage_bonus": 3
		}],
		"type": "Bludgeoning",
		"count": 4,
		"has_adv": False,
		"Special": ""
	},
	"black bear": {
		"name": "Black Bear",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d6",
			"damage_bonus": 2
		}, {
			"to_hit": 4,
			"damage_roll": "2d4",
			"damage_bonus": 2
		}],
		"type": "Piercing and Slashing",
		"count": 4,
		"has_adv": False,
		"Special": ""
	},
	"croocodile": {
		"name": "Crocodile",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d10",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"count": 4,
		"has_adv": False,
		"Special": "Hit: the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the crocodile can't bite another target."
	},
	"giant goat": {
		"name": "Giant Goat",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "2d4",
			"damage_bonus": 3
		}],
		"type": "Bludgeoning",
		"count": 4,
		"has_adv": False,
		"Special": "Charge. If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 5 (2d4) bludgeoning damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
	},
	"giant sea horse": {
		"name": "Giant Sea Horse",
		"attacks": [{
			"to_hit": 3,
			"damage_roll": "1d6",
			"damage_bonus": 1
		}],
		"type": "Bludgeoning",
		"count": 4,
		"has_adv": False,
		"Special": "Charge. If the sea horse moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. It the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone."
	},
	"giant wasp": {
		"name": "Giant Wasp",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d6",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"count": 4,
		"has_adv": False,
		"Special": "Hit: the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
	},
	"reef shark": {
		"name": "Reef Shark",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "1d8",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"count": 4,
		"has_adv": True,
		"Special": ""
	},
	"warhorse": {
		"name": "Warhorse",
		"attacks": [{
			"to_hit": 6,
			"damage_roll": "2d6",
			"damage_bonus": 4
		}],
		"type": "Bludgeoning",
		"count": 4,
		"has_adv": False,
		"Special": "Trampling Charge. If the horse moves at least 20 feet straight toward a creature and then hits it with a hooves attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked prone. If the target is prone, the horse can make another attack with its hooves against it as a bonus action."
	},
	"brown bear": {
		"name": "Brown Bear",
		"attacks": [{
			"to_hit": 6,
			"damage_roll": "1d8",
			"damage_bonus": 4
		}, {
			"to_hit": 6,
			"damage_roll": "2d6",
			"damage_bonus": 4
		}],
		"type": "Piercing and Slashing",
		"count": 2,
		"has_adv": False,
		"Special": ""
	},
	"dire wolf": {
		"name": "Dire Wolf",
		"name_plural": "Dire Wolves",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "2d6",
			"damage_bonus": 3
		}],
		"type": "Piercing",
		"count": 2,
		"has_adv": True,
		"Special": "Hit: If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
	},
	"giant eagle": {
		"name": "Giant Eagle",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "1d6",
			"damage_bonus": 3
		}, {
			"to_hit": 5,
			"damage_roll": "2d6",
			"damage_bonus": 3
		}],
		"type": "Piercing and Slashing",
		"count": 2,
		"has_adv": False,
		"Special": ""
	},
	"giant hyena": {
		"name": "Giant Hyena",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "2d6",
			"damage_bonus": 3
		}],
		"type": "Piercing",
		"count": 2,
		"has_adv": False,
		"Special": "Rampage. When the hyena reduces a creature to 0 hit points with a melee attack on its turn, the hyena can take a bonus action to move up to half its speed and make a bite attack."
	},
	"giant octopus": {
		"name": "Giant Octopus",
		"name_plural": "Giant Octopuses",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "2d6",
			"damage_bonus": 3
		}],
		"type": "Bludgeoning",
		"count": 2,
		"has_adv": False,
		"Special": "Hit: If the target is a creature, it is grappled (escape DC 16). Until this grapple ends, the target is restrained, and the octopus can't use its tentacles on another target."
	},
	"giant spider": {
		"name": "Giant Spider",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "1d8",
			"damage_bonus": 3
		}],
		"type": "Piercing",
		"count": 2,
		"has_adv": False,
		"Special": "Hit: the target must make a DC 11 Constitution saving throw, taking 9 (2d8) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
	},
	"giant toad": {
		"name": "Giant Toad",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "2d10",
			"damage_bonus": 2
		}],
		"type": "Piercing and Poison",
		"count": 2,
		"has_adv": False,
		"Special": "Hit: the target is grappled (escape DC 13). Until this grapple ends, the target is restrained, and the toad can't bite another target."
	},
	"giant vulture": {
		"name": "Giant Vulture",
		"attacks": [{
			"to_hit": 4,
			"damage_roll": "2d4",
			"damage_bonus": 2
		}, {
			"to_hit": 4,
			"damage_roll": "2d6",
			"damage_bonus": 2
		}],
		"type": "Piercing",
		"count": 2,
		"has_adv": True,
		"Special": ""
	},
	"lion": {
		"name": "Lion",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "1d8",
			"damage_bonus": 3
		}],
		"type": "Piercing",
		"count": 2,
		"has_adv": True,
		"Special": "Pounce. If the lion moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the lion can make one bite attack against it as a bonus action."
	},
	"tiger": {
		"name": "Tiger",
		"attacks": [{
			"to_hit": 5,
			"damage_roll": "1d10",
			"damage_bonus": 3
		}],
		"type": "Piercing",
		"count": 2,
		"has_adv": False,
		"Special": "Pounce. If the tiger moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the tiger can make one bite attack against it as a bonus action."
	}
}

### Error handling
if len(args) < 1:
	T = "Unrecognized input"
	D = "Need at least 1 input"
	animal_choices = []
	for key in animals:
		animal_info = animals[key]
		if animal_info["count"] == 6:
			animal_choices.append(animal_info)
	random_choice = randint(len(animal_choices))
	F = "If you're looking for a random CR 1/4 beast to conjure, may I suggest: " + animal_choices[random_choice]["name"]
	rolledInit = randint(20)+1
	rolledInit += animal_choices[random_choice]["init_mod"]
	F += "\nRolled initiative: " + str(rolledInit) + " [+" + str(animal_choices[random_choice]["init_mod"]) + "] modifier"
	return ""
animal_input = args[0].lower()
if animal_input not in animals:
	T = "Unrecognized input"
	D = "We did not find a creature named " + animal_input
	D += "\nExpected one of: "
	for key in animals:
		D += key + ", "
	D = D[:-2]
	F = ""
	return ""

### Input handling
override_quantity = []
override_advantage = False
override_disadvantage = False
target_ac = 0
to_hit = 0
for index, arg in enumerate(args):
	if index == 0:
		continue
	if arg.isdigit():
		override_quantity.append(int(arg))
	if arg[:2].lower() == "ac":
		target_ac = int(arg[2:])
	if arg.lower() == "adv":
		override_advantage = True
	if arg.lower() == "disadv":
		override_disadvantage = True
	if arg[:1] == "+":
		to_hit += int(arg[1:])
	if arg[:1] == "-":
		to_hit -= int(arg[1:])

animal_info = animals[animal_input]
if animal_info["has_adv"]:
	override_advantage = True
if override_advantage and override_disadvantage:
	override_advantage = False
	override_disadvantage = False
if len(override_quantity) == 0:
	override_quantity.append(animal_info["count"])

### Printing title, ensure it properly echos input for sanity
if len(override_quantity) > 1 or (len(override_quantity) == 1 and override_quantity[0] > 1):
	if "name_plural" in animal_info:
		animal_info["name"] = animal_info["name_plural"]
	else:
		animal_info["name"] += "s"

quantity = ",".join(str(x) for x in override_quantity)
T = quantity + " conjured " + animal_info["name"] + " attack"
if override_advantage:
	T += " with advantage!"
elif override_disadvantage:
	T += " with disadvantage!"
else:
	T += "!"

if to_hit > 0:
	T += " [+" + str(to_hit) + " to hit]"
if to_hit < 0:
	T += " [" + str(to_hit) + " to hit]"

### Computation
D = ""
for index, quant in enumerate(override_quantity):
	#Result is a array of arrays of 3 elements: [hits, nat20, damage]
	#They represent AC scores from 11 to 20, unless target_ac is greater than 0, in which case the size is 1.
	results = []
	if target_ac > 0:
		results.append([0, 0, 0])
	else:
		for i in range(11, 21):
			results.append([0, 0, 0])

	for i in range(quant):
		for an_attack in animal_info["attacks"]:
			initial_roll = randint(20)+1
			if override_advantage:
				new_roll = randint(20)+1
				initial_roll = max(initial_roll, new_roll)
			if override_disadvantage:
				new_roll = randint(20)+1
				initial_roll = min(initial_roll, new_roll)
			natural_20 = False
			if initial_roll == 20:
				natural_20 = True
			if initial_roll == 1:
				continue

			initial_roll += an_attack["to_hit"] + to_hit

			#Damage roll
			dice_to_roll_string = an_attack["damage_roll"] + "+" + str(an_attack["damage_bonus"])
			if natural_20:
				dice_to_roll_string += "+" + an_attack["damage_roll"]
			damage = vroll(dice_to_roll_string).total

			if target_ac > 0:
				if initial_roll >= target_ac or natural_20:
					# Hit target AC
					if natural_20:
						results[0][0] += 1
						results[0][1] += 1
					else:
						results[0][0] += 1
					results[0][2] += damage
			else:
				for j, AC in enumerate(range(11, 21)):
					if initial_roll >= AC or natural_20:
						#Hits this AC
						if natural_20:
							results[j][0] += 1
							results[j][1] += 1
						else:
							results[j][0] += 1
						results[j][2] += damage
					else:
						# Will never hit the remaining AC
						continue

	# Print results
	D += str(quant) + " " + animal_info["name"] + " does " + animal_info["type"] + " damage:"
	if target_ac > 0:
		D += "\n" + str(target_ac) + "AC: " + str(results[0][0]) + " hits, " + str(results[0][1]) + " crits, " + str(results[0][2]) + " damage."
	else:
		for i, AC in enumerate(range(11, 21)):
			D += "\n" + str(AC) + "AC: " + str(results[i][0]) + " hits, " + str(results[i][1]) + " crits, " + str(results[i][2]) + " damage."

	if index < len(quantity) - 1:
		D += "\n\n"

F = animal_info["Special"]
</drac2>
-title "{{T}}"
-desc "{{D}}"
-footer "{{F}}"