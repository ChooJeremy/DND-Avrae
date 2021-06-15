# DND-Avrae

This repository contains scripts written in Draconic, Avrae's coding language, to be saved as aliases.

They are used in order to keep DND games going smoothly during game time, speeding up typical tasks that can drag out combat.

## Conjure Animals

This script automate the attack of conjure animals

Usage:
```
!ca [animal] [args]
```
Where args can be, in any order:
* "adv": Rolls with advantage
* "disadv": Rolls with disadvantage
* "acX", where X is a number: Only displays results of ac X rather than from 11 to 20.
* "X", where X is a number: Sets group size to X rather than the default number. You may specific multiple instances of ths parameter.

All arguments are case-insensitive.
If animal contains multiple words, you must wrap them in quotes (") i.e. `!ca "giant poisonous snake"`

Sample usage:
`!ca wolf`
```
8 conjured Wolves attack with advantage!
8 Wolves does Piercing damage:
11AC: 7 hits, 0 crits, 47 damage.
12AC: 7 hits, 0 crits, 47 damage.
13AC: 6 hits, 0 crits, 37 damage.
14AC: 5 hits, 0 crits, 32 damage.
15AC: 4 hits, 0 crits, 24 damage.
16AC: 3 hits, 0 crits, 18 damage.
17AC: 2 hits, 0 crits, 13 damage.
18AC: 2 hits, 0 crits, 13 damage.
19AC: 2 hits, 0 crits, 13 damage.
20AC: 1 hits, 0 crits, 7 damage.
Hit: if the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone.
```
Wolves have advantage by default due to pack tactics.

`!ca elk 4 4 ac15`
```
4,4 conjured Elks attack!
4 Elks does Bludgeoning damage:
15AC: 2 hits, 0 crits, 19 damage.

4 Elks does Bludgeoning damage:
15AC: 4 hits, 0 crits, 34 damage.
Charge. If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.
```
Here, Elks split into 2 groups and attack 2 different enemies, both with AC 15.
The extra damage from Charge is not computed normally, it has to be added in (typically add hits * 7)
Note that the script doesn't take into account enemies failing on the saving throw and being knocked prone (thus remaining attacks would be at advantage). If you want to take this into account, you need to roll at smaller numbers, i.e. `!ca elk 2`, `!ca elk 2`. Suppose the 2nd group causes a failed saving throw, then do `!ca elk 4 adv` to roll the reminader with advantage.