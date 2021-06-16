!alias toad embed
<drac2>
args = &ARGS&
if len(args) == 0:
	T = "Unknown input"
	D = "Expected either: bite or swallow"
	F = ""
	return ""

if args[0].lower() == "bite":
	T = "Giant Toad: Bite"
	D = "Hit: The target is grappled (escape dc 13) Until this grapple ends, the target is restrained, and the toad can't bite another target."
	F = "Grappled\nA grappled creature’s speed becomes 0, and it can’t benefit from any bonus to its speed.\nThe condition ends if the Grappler is incapacitated (see the condition).\nThe condition also ends if an Effect removes the grappled creature from the reach of the Grappler or Grappling Effect, such as when a creature is hurled away by the Thunderwave spell.\n\nRestrained\nA restrained creature’s speed becomes 0, and it can’t benefit from any bonus to its speed.\nAttack Rolls against the creature have advantage, and the creature’s Attack Rolls have disadvantage.\nThe creature has disadvantage on Dexterity Saving Throws."
	return ""

if args[0].lower() == "swallow":
	T = "Giant Toad: Swallow"
	D = "Swallow. The toad makes one bite attack against a Medium or smaller target it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the toad, and it takes 10 (3d6) acid damage at the start of each of the toad's turns. The toad can have only one target swallowed at a time. If the toad dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone."
	F = "Blinded\nA blinded creature can’t see and automatically fails any ability check that requires sight.\nAttack Rolls against the creature have advantage, and the creature’s Attack Rolls have disadvantage."
	return ""

T = "Unknown input"
D = "Expected either: bite or swallow"
F = ""
return ""
</drac2>
-title "{{T}}"
-desc "{{D}}"
-footer "{{F}}"