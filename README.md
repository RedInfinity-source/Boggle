# Boggle

The code is a Python word game using the Ursina game engine. It generates a 4x4 grid of cubes with random alphabet letters, players input words, and the game checks if the word is valid. If valid, players earn points based on length and letter scores. The game includes a timer, points counter, grid, input field, submit button, and word validation logic. Players aim to maximize their score by forming valid words.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)
- [Rating: 6/10](#Rating)

# About

The code is a Python word game that uses the Ursina game engine to generate a 4x4 grid of cubes with random alphabet letters. Players input words using an input field and submit them to the game. The game checks if the word is valid (at least 3 letters long and exists in the English dictionary), and if it is, the player earns points based on the word's length and letter scores. The game includes a timer, points counter, grid of cubes, input field, submit button, and word validation and scoring logic. The game continues until the time limit is reached, and players aim to maximize their score by forming valid words using the available letters.

# Features

The Ursina game engine is a Python-powered, open-source game engine built on top of the Panda3D game engine. Key features include hot reloading, automatic import, fullscreen development, procedural geometry, built-in animation and tweening, pre-made prefabs, procedural 3D primitives, and custom shaders.

The game mechanics include a 4x4 grid of cubes with random alphabet letters, an input field for players to input words, a submit button for word submission, word validation, scoring logic, timer and points counter, game flow, and user interface (UI). Players aim to maximize their score by forming valid words using available letters.

User interface (UI) should be clean and intuitive, using Ursina's capabilities to create sleek and modern elements. Edge cases, such as handling invalid words, displaying feedback, and providing a satisfying user experience, should be handled.

For more details on implementing specific features or troubleshooting, refer to the Ursina documentation at https://www.ursinaengine.org/. Your Python word game has the potential to be both fun and educational, and you can find more information on implementing specific features or troubleshooting by visiting the Ursina documentation.

# Imports

random, ursina, enchant, PyDictionary

# Rating

The game has a clear objective, a timer, and rewards points based on word length. It uses tooltips for word definitions and feedback. The graphical interface is simple. However, it could benefit from better organization, modularization, clearer variable names, improved error handling, and clearer feedback. It also lacks sound effects or music, and could benefit from more appealing graphics and animations.
