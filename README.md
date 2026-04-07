# reactiontimememorygame_BCS200-FinalProject-
BCOG 200 final project
check in #2: 
# Reaction Time Memory Game

## Overview
This project is a Python program that includes small cognitive mini-games focused on reaction time and short-term memory. The user will interact with the program through the terminal and complete different challenges that test their speed and memory. The program will record results from each round and calculate simple performance statistics. The goal of the project is to create an interactive cognitive game using Python while practicing loops, conditionals, modular design, and testing.

## Why someone would use this program
A user could use this program to try simple brain-training style games and see how well they perform. It can also be used as a fun demonstration of how reaction time and short-term memory tasks can be modeled in Python.

## Planned Files
- `README.md` — project documentation and instructions
- `main.py` — main Python script containing the game logic
- `tests/test_project.py` — unit tests for helper functions

## Planned Functions

### generate_sequence(length)
Parameter:
- `length` (int): the number of digits in the sequence

This function generates a random sequence of digits for the memory test.

### run_memory_test(length)
Parameter:
- `length` (int): the number of items the user must remember

This function displays a sequence for the user to memorize, then checks whether the user's response matches the original sequence.

### run_reaction_test(rounds)
Parameter:
- `rounds` (int): the number of reaction rounds to run

This function waits a random amount of time, prompts the user to respond, and records reaction times for multiple rounds.

### summarize_results(reaction_times, memory_score)
Parameters:
- `reaction_times` (list): list of reaction times from the reaction test
- `memory_score` (int): number of correct memory responses

This function calculates summary statistics and displays the user's performance.

## Example Use Cases
- A user wants to test their reaction time over several rounds.
- A user wants to try a short memory challenge.
- A user wants to see a final summary of their performance after both games.

## How to Run
Run the project in the terminal with:

```bash
python3 main.py

