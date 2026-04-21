# Reaction Time Memory Game

## Overview
This project is a Python-based GUI game that tests two basic cognitive skills: reaction time and short-term memory. Instead of running only in the terminal, the game opens in a Tkinter window and guides the user through interactive tasks.

The first part of the game measures how quickly the user responds to a visual signal. The second part tests short-term memory by asking the user to memorize and recall a sequence of numbers. After both tasks are completed, the program displays a final results screen summarizing the user's performance.

## Purpose
This project connects programming with cognitive science by modeling two simple experimental tasks often used in psychology and neuroscience:

- Reaction time task
- Short-term memory recall task

It was designed to be a simple but engaging interactive application while demonstrating core Python programming skills.

## Features
- Opens in a popup GUI window using Tkinter
- Runs multiple reaction-time rounds
- Uses randomized delays before the reaction signal appears
- Measures reaction times accurately
- Includes a short-term memory challenge
- Displays final performance results
- Allows the user to play again without restarting the program

## File Structure
- `README.md` — project documentation
- `main.py` — main game code and GUI logic
- `tests/test_project.py` — unit tests for helper functions

## Approach
This project was designed using a modular approach. Each major part of the game is handled by a separate function or method.

The reaction-time portion uses randomized wait times and timing functions to simulate a basic response-speed task. The memory portion generates a random number sequence and checks whether the user's recalled answer matches it. The GUI was built with Tkinter so that the program opens in a separate application window rather than relying only on terminal input.

The design focused on creating a minimal viable product first, with the core game logic working before adding interface improvements such as replay support and a clearer results screen.

## Main Functions
### `generate_sequence(length)`
Generates a random list of digit strings for the memory task.

### `calculate_average(values)`
Computes the average of a list of numbers.

### `check_memory_answer(user_answer, sequence)`
Checks whether the user's typed memory response matches the original sequence.

### `main()`
Creates the Tkinter window and starts the game.

## How to Run
Make sure Python 3 is installed on your computer. Then run:

```bash
python3 main.py