# Boggle
The project uses Pygame to digitally execute Boggle, a classic word game where players form words from adjacent letters, competing against a computer to find valid words within a set time.

[![Static Badge](https://img.shields.io/badge/nltk-orange)](https://pypi.org/project/nltk/)
[![Static Badge](https://img.shields.io/badge/random,-green)](https://pypi.org/project/random,/)
[![Static Badge](https://img.shields.io/badge/pygame-gray)](https://pypi.org/project/pygame/)
[![Static Badge](https://img.shields.io/badge/nltk-pink)](https://pypi.org/project/nltk/)

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

The project is a digital version of Boggle, a word game developed using Pygame. Players form words from adjacent letters on a random 4x4 board, competing against a computer to find as many valid words as possible within a set time.

## Features

- Random Letter Board: A 4x4 grid of randomly generated letters.
- Word Validation: Ensures words are valid based on a dictionary from NLTK.
- Multiline Input: Allows players to input multiple words.
- Timer: Tracks the time for each round.
- Scoring System: Calculates points for valid words based on their length and complexity.
- Computer Opponent: Competes against the player by generating its own words.
- Restart Button: Allows the player to restart the game.

## Installation

Prerequisites
- Python 3.6 or higher
- Reddit API credentials
- Wikipedia API library
- Holidays library
- Pycountry library

Prerequisites
- Python 3.x
- Pygame
- NLTK

## Usage

Run the game:
- python main.py

Playing the game:
- The game starts with a random 4x4 letter board.
- Enter words using the multiline input box.
- Words must be at least 3 letters long and formed from adjacent letters.
- Press the "Play" button to start a new game.
- The game automatically ends a round every 3 minutes and updates the scores.
- The game continues until either the player or the computer reaches the target score (50 or 100 points).

## Contributing

Contributions are welcome! To contribute to Monster Maze, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
