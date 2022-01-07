---
Title: About project
Description: MinecraftPlus
Author: Wituch

Template: tmpl/index
Language: en

Date: 2020-08-10
Order: 0
---

# What is Minecraft Plus?

**MinecraftPlus** *(Minecraft +, MC+)* is a comprehensive project aimed at creating an improved version of the standard game **Minecraft** by **Mojang**.

Modifications made as part of the project include a part of the client and server, which allows you to use MC+ to run a fully functioning server, available to every player using MC+.

To properly understand the idea of ​​the project, you need to distinguish between two concepts - **modification for Minecraft** and **modified Minecraft**. This project is the latter.

# Why was this project created?

MC+ is the result of combining the sentiment for the game with passion and ambitions aimed at creating something "bigger" that sums up all activities related to Minecraft.
You can justify all this by wanting to leave a trace of your activity in such a huge community that Minecraft players create and at the same time not let all the time devoted to servers, plugins, game engine and libraries not be locked in a drawer and lost.

# Why MC+ when the Internet is full of mods for everything?

It cannot be denied that Minecraft modifications made available on the Internet by various developers are often masterpieces, developing the game with all sorts of things. In fact, you can find mods for anything (okay, almost anything).

However, without delving into the pros of such modifications, and focusing on the minuses - the biggest problems with autonomous modifications are:
- their compatibility, which is of great importance with a large number of modifications
- supporting a given version of Minecraft
- client and server side support

For sure, everyone who has had contact with modded servers has experienced the problems that can arise when using popular mods.
In my subjective opinion (you may agree) the main problem is ultimately the sheer volume of changes that these modifications introduce. Often times, there is an ideal mod with a functionality that interests us - but beyond that, it has more functionality that we don't need.

This is why this project was created, to tailor the best changes to specific needs, without unnecessary functionalities that only hinder the game, especially for newcomers.

# What software is included in the project?

The project includes:
- MinecraftPlus-Client - game client application with modifications
- MinecraftPlus-Server - game server application with modifications
- SpigotPlus-Server - game server application with modifications and Spigot API * allowing to run plugins
- SpigotPlus-API - Spigot API supplemented with modifications from the project
- AuthServerLibrary\*\* - a library that allows you to authorize players on the server without plugins (replacement for AuthLib)

\* integration with PaperMC is expected in case of greater demand  
\*\* currently unavailable

# Who is the project intended for?

Due to the nature of the modifications, which focus mainly on expanding the survival mechanisms, expanding the available ores, materials, recipes, methods of production, processing, etc., the project is aimed mainly at players and server developers who maintain the game in a ** survival ** atmosphere ( look down).
Apart from universal changes that would actually fit any type of server, the project is focused on developing functionalities that have always been a problem for RPG servers (see below).

So if you like to play or create a server in a survival atmosphere, especially with **RPG** elements (see below), this project is perfect for you!

# Why is this design fit for Survival servers?

The answer to this question is my subjective opinion based on many years of experience, my own ideas and ambitions.

Namely, the survival served to us by the default version of the game is a very simplified version of the real survival. I want to breathe more natural mechanisms into the game, requiring the player to pay more attention to detail and to survive. So that the gameplay is not based on mindless recreating patterns (excavate-process-own) but planning the direction of the game in often contradictory directions to differentiate players.
Such differentiation is expected to increase the integration of players and increase the number of interactions, due to the significantly reduced independence of players. Which does not mean that it will be impossible to survive on your own - but it will be very demanding.

It is impossible to present here the whole system, which is to consist of a series of specific changes, complementing each other. Let me just give you an example that first came to mind: diseases and injuries requiring the intervention of a physician (skilled player) and / or the use of medications (made by a skilled player) - which for a hand-to-hand combat character would be a lethal threat without an external help. Or maybe until when a given character manages to acquire the appropriate skills ...?

# Why is this design suitable for RPG servers?

The answer to this question is my subjective opinion based on the observation of various servers trying to build RPG gameplay. Here is what, in my opinion, is the most important.

No RP / RPG server can do without the possibility of shaping its character and differentiating it from others. The most popular solution commonly used by servers of this type are classes and skill trees. Despite good ideas, their implementation with plugins often leaves a lot to be desired.
The project will offer a solution to this problem by native support of the skill tree with the possibility of managing development points, allowing you to choose a character development path, on which the character's abilities, strengths and weaknesses will depend.

Another weak point of RP servers is the creation of an appropriate NPC system with the possibility of interaction, mainly conversations and quests.
There are plugins that allow you to implement dialogue options and bind them to quests, etc., however, the visual reception is often hampered by the use of in-game chat.
The project will offer native support for interacting with NPCs through appropriately prepared interfaces (GUI views), relieving the creators from technical problems, allowing them to focus on creating content, not systems.

# How to use MC+?

If you want to run the client or server on MiecraftPlus, you need to download the appropriate installer from the [Download](download) section.
There you will find information on where and how to download the appropriate version configuration to run the MC+ client or server.

# Plans for the future

The next steps planned for the project are:
- building a trusted community interested in using MC+
- creating an installer that allows you to use [delta files](https://www.techwalla.com/articles/what-is-a-delta-file) to generate MC+ executable
- replacing the installer with a launcher that automates the installation of MC+
- integration of planned modifications.

The list of planned modifications is long (and contains only the most important ideas), it is not easy to define a specific course of work. Therefore, as mentioned earlier:

> In order to collect feedback from the community and test interest, I first released a demonstration modification [Cannon Update](updates/released/cannon-update) that adds cannons, mortars and cannonballs to the game. The modification is supposed to be a solution to the unsightly realization of "cannons" by using TNT.

In short, the future of this project depends only on its reception by a wider group of players and Minecraft server developers.
