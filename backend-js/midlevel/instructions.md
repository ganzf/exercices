# Instructions

*Deep within the mountains lies a legendary artifact, said to be capable of granting immense power to whoever possesses it. Many adventurers have set out in search of this artifact, but none have returned. Now, a new group of brave heroes have gathered to embark on the perilous journey to uncover the artifact and unlock its secrets. Will they succeed where others have failed, or will they meet the same fate as those who came before them?*

## Prerequisites

-- You must have yarn or npm installed on your computer
-- Run yarn or npm install in the midlevel directory
-- You should install the Jest runner extension in your visual studio code if you don't have it
-- If there are errors during the setup, please ask for help

## Exercice 01

- Open file `ex01/step1.ts`
- Write a function `waaagh` that takes a single parameter `orcs` of type `number` and returns a list of strings.
- If there are no orcs, the list should be empty
- Each orc will have something to say, and the first string in the list will be what the first orc said. For example orc#1 says "duh.", the list should start with `["duh.", ...]`
- Each orc has a number, and what the orc says depends on his number.
- If the number is a multiple of 5, the orc says `"grumbl"`
- If the number is a multiple of 3, the orc says `"zock"`
- If the number is a multiple of 3 and 5, the orc says "`grumblzock`"
- If the number is none of the above, the orc just says `"waagh"` followed by his number (ex: `"waagh14"`)
- (bonus) If the number is 69, the orc says `"nice."`
- The first orc has the number 1 (there are no orc#0)

Success condition: `yarn test step1`

## Exercice 02 (~10 minutes)

- Open file `ex02/step2.ts`
- Write a function `organizeBattle` that takes a list of orcs as parameter and will return a list of Orc Battalion
- An orc has a number and a warriorType (it must be a literal 'Melee', 'Ranged' or 'Dummy')
- An orc Battalion is a group of orcs. It must be no bigger than 9 orcs. It is organized in 3 rows of 3.
- The goal of the function organizeBattle is to take all orcs and organize them in the best possible battalions
- The score of a battalion is computed as follows:
  - Battalions must have all 3 types
  - Battalions must be full
  - Ranged should be on row 3
  - Melee should be on row 1
  - Dummy can be anywhere
  - There can be no more than 3 Ranged in a battalion
- A battalion must have a method getRow1(), getRow2() and getRow3() that will respectively return the types of orcs on the row
  - example: `getRow2() => ['Melee', 'Ranged', 'Melee']`
- Your goal is to create as many battalions has possible with the given orcs

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

You should implement the HTTP API in Node.js using TypeScript. You should also write unit tests for each of the API routes using a testing library like Jest. Finally, you should ensure that your API code is memory-efficient by using techniques like object pooling or limiting the use of closures and anonymous functions.

Here are some additional requirements and constraints for the exercise:

You should use an in-memory data store to store the player data. You do not need to persist the data to disk.
You should use an appropriate HTTP library to handle incoming requests and outgoing responses. Express.js is a popular choice, but you are free to use any library you are comfortable with.
You should use TypeScript to define the data types for the player objects and the API routes.
You should use Jest to write unit tests for the API routes.

### Mid-Level

Players should gain xp over time. Every 10 seconds a player should level up.
Until it reaches level 5.

### Advanced

Setup a websocket server. You are free to test your websocket server however you want (curl, custom js script, react app...). Your websocket server should send a websocket event to all clients when a player levels up.