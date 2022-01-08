---
Title: Block Mechanics Update
Description: Update changing the way blocks are broken
Author: Wituch
Date:

Template: tmpl/updates/update-page

Dependencies:
    - id: Character Update
      desc: Due to the influence of the character's statistics (e.g. strength) on the amount of "damage" dealt - similarly, the stronger character of the player hits with greater force
      type: dependent
    - id: Cannon Update
      desc: By being able to stack damage dealt by cannonballs
      type: extension
---

# Block Mechanics Update - new rules
-----

The update is to introduce a completely new look at the functioning of blocks in the game - each block will be able to store information about received damage.

In the original version, each extractable block has a certain "hardness" that defines the time needed to extract a block with a tool made of a specific material. For example, for any block of wood, its cutting with an iron ax takes 0.5 seconds(according to Minecraft Wiki).
The case is completely different in the case of harder blocks, e.g. obsidian, which takes 9.4 seconds to extract using a diamond ax. If we stop mining while mining obsidian, all progress is lost...

> What if you made mining a specific block require enough "damage" to mine it?

Each block will have a specific durability (maximum block "HP"). As you take damage and lower the "HP" level, progressive traces of destruction will appear on the block (as in the original release, when digging). When the "HP" level of a block drops to 0 or less, it will be picked up (eg with an ax, pickaxe) or destroyed (eg by an explosion) depending on the source of the damage.

When using tools to extract blocks (which applies to all blocks, not just raw materials), each use (movement) of the tool causes its gradual wear.


# Advantages of the modification
 - greater realism of extraction (each movement of the tool does a specific job, without senseless waving)
 - the ability to easily scale the extraction ability through character statistics, e.g. strength
 - the possibility of cooperation of several players while extracting the same block
 - synergy with the modification that adds cannons, thanks to the ability to build strong fortifications (requiring several hits to pierce)
 - the possibility of implementing erosion over time, blocks damaged above a certain block limit, e.g. bricks in fortifications as well as "self-healing", e.g. sand blocks
