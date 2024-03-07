# Boggle

The code is a Python word game using the Ursina game engine. It generates a 4x4 grid of cubes with random alphabet letters, players input words, and the game checks if the word is valid. If valid, players earn points based on length and letter scores. The game includes a timer, points counter, grid, input field, submit button, and word validation logic. Players aim to maximize their score by forming valid words.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)

## About

The code is a Python word game that uses the Ursina game engine to generate a 4x4 grid of cubes with random alphabet letters. Players input words using an input field and submit them to the game. The game checks if the word is valid (at least 3 letters long and exists in the English dictionary), and if it is, the player earns points based on the word's length and letter scores. The game includes a timer, points counter, grid of cubes, input field, submit button, and word validation and scoring logic. The game continues until the time limit is reached, and players aim to maximize their score by forming valid words using the available letters.

## Imports

random, ursina, enchant, PyDictionary
