---
Title: Biome Update
Description: Update regulating the presence of resources, plants and animals on the map depending on the biome
Author: Wituch
Date:

Template: tmpl/updates/update-page

Dependencies:
    - id: Dep Update
      desc: desc of dependency
      type: dependent
    - id: Character Update
      desc: Through the influence of the biome in the area where the player's character is located, e.g. a drastic drop in body temperature in cold, snowy biomes
      type: extension
    - id: Food Update
      desc: By better regulating the presence of plants in different areas of the map, depending on the biome
      type: extension
    - id: Animal Update
      desc: By better regulating the presence of animals in different areas of the map, depending on the biome
      type: extension
---

# Biome Update - differentiating map areas
-----

In the original release of the game, the differentiation between areas depending on the biome that occurs on them is noticeable even in such basic cases as sand. In the desert biome it will be found everywhere in enormous amounts, and in the lowland biome in small amounts, mainly near bodies of water. Another example is the emerald, which is restricted to mountain biomes.
In the case of other raw materials such as coal, it is not the same anymore. Coal in the game is the most common deposit in the game and can be found virtually anywhere on the map. Such a situation results in a low value of this raw material, which is not necessarily justified from the point of view of suitability.

> Appropriate differentiation of the availability of goods depending on the region of the map will increase the importance of territorial control, which translates into access to the appropriate goods.

The situation is similar in the case of vegetation and animals. It is true that the natural occurrence is limited in many cases (e.g. bamboo only near water reservoirs, polar bears only in winter biomes) but there are no restrictions when it comes to transporting them to another place. At any time, we can collect the bamboo we find and plant it in another biome. Same with animals - once you've found your desired cow park, you can raise them in the desert.

The modification is aimed at regulating the above-mentioned mentioned and other cases. The regulation is to consist in assigning appropriate blocks of resources and creatures to biomes, adjusting their quantity (rarity) and conditions of occurrence (e.g. chunk height ranges for blocks). In the case of animals, the ability to survive in a given biome will be regulated (e.g. a polar bear will not survive in the desert) or to function in a given biome (e.g. a cow will not give birth to young calves in the desert).

# Advantages of modification
 - diversity of areas in terms of attractiveness and usefulness
 - territorial control is gaining importance in securing the sources of raw materials
