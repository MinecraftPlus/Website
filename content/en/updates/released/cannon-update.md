---
Title: Cannon Update
Description: An update that adds cannons and cannonballs to the game that allow for artillery fire
Author: Wituch
Date: 29-10-2020

Template: tmpl/updates/update-page

Dependencies:
    - id: Block Mechanics Update
      desc: By changing the block destruction system, where a block receives insufficient damage from a projectile hit to destroy it, keeping this information (a block shows a trace of damage, cracks). If the block takes more damage, it will add up to the previous damage, and if it exceeds the block's durability, it will be destroyed.
      type: dependent
    - id: Interactions Update
      desc: By changing the interaction system allowing for more convenient use and operation of the guns.
      type: dependent
---

# Cannon Update - briefly about the demo modification
-----

This is the first update to showcase the capabilities of the entire * MinecraftPlus * project.

Cannonballs and cannonballs have been added to the game in this update. With the addition of guns, the nature of TNT has changed, and its time to detonation is reduced when it comes into contact with the blast.

> Due to the fact that in multiplayer games the rivalry between groups is the driving force of good gameplay, I think that this solution to the problem will appeal to many players.



# Cannon

<div style="padding: 10pt 0;">
    <img src="%assets_url%/images/cannon-update_cannon-front.png" style="width: 49%;">
    <img src="%assets_url%/images/cannon-update_cannon-back.png" style="width: 49%;">
</div>

## Crafting works

<img src="%assets_url%/images/cannon-update_cannon-crafting.png" style="float: right; margin-left: 20pt;">
The recipe for crafting a cannon is a shape recipe.

Recipes with all plank variants are available.
</br>
</br>
</br>


# Missiles

<img src="%assets_url%/images/cannon-update_cannonballs.png" style="float: right; margin-left: 20pt;">
The update adds two variants of artillery shells to the game - high-explosive and incendiary shells.

Demolition projectiles have a high penetration power and cause an explosion that deals a large amount of damage to the blocks they hit.
Incendiary projectiles have the ability to ignite the environment they strike. They do not have the piercing ability that would allow them to destroy strong fortifications, especially non-flammable ones.

## Projectile Crafting

<img src="%assets_url%/images/cannon-update_cannonball-crafting.png" style="float: right; margin-left: 20pt;">
A recipe for crafting cannonballs is also a shape recipe.

The incendiary cannonball recipe is a delicate variation on the demolition ball recipe - not shown, for the curious to discover.



# Servicing cannon

## Moving the cannon

The cannon gun added in the update has the nature of a vehicle like a boat or a cart. The player can take control of the cannon by clicking 'RMB' on the cannon.

Moving the cannon is analogous to that of a character - 'left / right' rotates the cannon and 'forward / back' allows you to push the cannon forward or pull it back.

To change the angle of the barrel, use the 'forward / backward' movement with the 'jump' key pressed. The 'front' direction raises the barrel up, the 'back' direction brings it down.

<center>
    <video width="80%" controls>
      <source src="%assets_url%/videos/cannon-update_cannon-steering.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</center>
</br>

## Loading and firing works

The basic way to load a gun is to "throw" the desired amount of gunpowder and the cannonball into the barrel of the gun.
As an indicator of readiness to fire there is a fuse fuse on the rear of the barrel. Ready to fire does not require loading a cannonball!

To load gunpowder or a bullet into a gun, stand in front of it, aim at the barrel opening and, holding the item to be loaded in your hand, click 'RMB'.
To shoot, stand behind the cannon, aim at the fuse and, holding a torch, click RMB.

<center>
    <video width="80%" controls>
      <source src="%assets_url%/videos/cannon-update_cannon-loading-and-shooting.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</center>
</br>

## Opening the menu works

In addition to the loading method of the gun by "throwing" an item into the barrel of the gun, it is possible to open the graphical menu of the gun. This menu allows you to load the cannon by transferring the gunpowder and cannonball to the appropriate slot.
This menu also allows you to unload the gun by removing the bullet - loaded gunpowder can no longer be recovered.

To open the graphical menu of the gun, click on the `RMB` on the gun while holding down the` sneak` key (by default: `left Shift`).

<center>
    <video width="80%" controls>
      <source src="%assets_url%/videos/cannon-update_cannon-menu-opening.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</center>
</br>



# Mortar

In the second version of the update, mortars have been added, which are an alternative to cannons that have mainly horizontal flight path - the mortar allows you to fire at an enemy hidden behind fortifications from the air.

<div style="padding: 10pt 0;">
    <img src="%assets_url%/images/cannon-update_mortar-front.png" style="width: 49%;">
    <img src="%assets_url%/images/cannon-update_mortar-back.png" style="width: 49%;">
</div>

## Crafting Mortar

<img src="%assets_url%/images/cannon-update_mortar-crafting.png" style="float: right; margin-left: 20pt;">
A recipe for crafting a mortar is a shape recipe. The only difference from the gun is that it requires one block of iron less.

Recipes with all variations of boards are available.
</br>

## Difference between a gun and a mortar

Mortars with Due to the shorter barrel, they have a lower throwing ability than the guns. Their design also limits the shooting angle. The mortar can also be loaded by standing behind it (on the side of the fuse), as long as the barrel is deflected properly.
Apart from these differences, the operation of the mortar is analogous to that of a gun.


# Advantages of the modification
  - increasing the realism of the sieges
  - control of the flight path by changing the angle of the barrel or the amount of powder
  - control of the obtained effects of fire by using high-explosive or incendiary projectiles
  - the possibility of using different fire strategies by changing the power of the shot or the type of projectile
  - mobility of siege machines


<div style="padding: 10pt 0;">
    <img src="%assets_url%/images/cannon-update_presentation.png">
</div>
