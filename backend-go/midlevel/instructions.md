# Instructions

*Deep within the mountains lies a legendary artifact, said to be capable of granting immense power to whoever possesses it. Many adventurers have set out in search of this artifact, but none have returned. Now, a new group of brave heroes have gathered to embark on the perilous journey to uncover the artifact and unlock its secrets. Will they succeed where others have failed, or will they meet the same fate as those who came before them?*

## Prerequisites

-- You must have go installed
-- If there are errors during the setup, please ask for help

## Exercice 01

- Open file `ex01/main.go`
- Implement the function `Grumblzock` that takes a single parameter `orcs` of type `number` and returns a list of strings.
- If there are no orcs, the list should be empty
- Each orc will have something to say, and the first string in the list will be what the first orc said. For example orc#1 says "duh.", the list should start with `["duh.", ...]`
- Each orc has a number, and what the orc says depends on his number.
- If the number is a multiple of 3, the orc says `"zock"`
- If the number is a multiple of 5, the orc says `"grumbl"`
- If the number is a multiple of 3 and 5, the orc says "`grumblzock`"
- If the number is none of the above, the orc just says `"waagh"` followed by his number (ex: `"waagh14"`)
- (bonus) If the number is 69, the orc says `"nice."`
- The first orc has the number 1 (there are no orc#0)

Success condition: Unit tests must pass.

## Exercice 02 (~10 minutes)

Open file `ex02/main.go`. Our goal is to prepare orcs for a battle.
Orcs can be warrior, archers or idiots.
Orcs must be organized in Battalions, a group of 9 orcs, no more, no less.
Write a function OrganizeBattle that takes a list of Orcs as parameter, and outputs a list of Battalions.

A battalion should have 9 orcs, 3 melee, 3 archers at the minimum.
Build your strongest army !

## Main Exercice

You are building an HTTP API for a simple role-playing game. The API should support the following routes:

```
GET /players        : Get a list of all players.
POST /players       : Create a new player.
GET /players/:id    : Get a specific player by their ID.
DELETE /players/:id : Delete a specific player by their ID.
```

Each player has the following properties:

```
id: a unique identifier for the player.
name: a string describing the player's name.
level: a number indicating the player's level.
gold: a number indicating the player's gold.
```

You should implement the HTTP API in go using any framework, preferably Gin Gonic. You should also write unit tests for each of the API routes.
You should use an in-memory data store to store the player data. You do not need to persist the data to disk.

### Mid-Level

Players should gain xp over time. Every 10 seconds a player should level up.
Until it reaches level 5.

### Advanced

You should make your data persistent, using the format you want, being able to restart your program and loading back the player information in memory.