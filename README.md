# Reaction Time Memory Game

## Overview
This project is a Python-based GUI game that tests three cognitive skills: reaction time, short-term memory, and attention. Instead of running only in the terminal, the game opens in a Tkinter window and guides the user through three interactive rounds.

The first round measures how quickly the user responds to a visual signal. The second round tests short-term memory by asking the user to memorize number sequences that get longer after each correct answer. The third round is a Stroop attention task where the user must type the color of a word instead of the word itself within a 30-second time limit.

After all three rounds are completed, the program displays a final results screen summarizing the user's reaction time, memory score, and Stroop score.

## Purpose
This project connects programming with cognitive science by modeling simple tasks often used in psychology and neuroscience:

- Reaction time task
- Short-term memory recall task
- Stroop attention task

It was designed to be a simple but engaging interactive application while demonstrating core Python programming skills such as functions, classes, conditionals, loops, randomization, timing, GUI design, and testing.

## Features
- Opens in a popup GUI window using Tkinter
- Includes clear instructions on the opening screen
- Runs multiple reaction-time rounds
- Uses randomized delays before the reaction signal appears
- Measures average and best reaction time
- Includes an adaptive memory challenge
- Makes the memory sequence one digit longer after each correct answer
- Ends the memory round when the user makes a mistake
- Includes a 30-second timed Stroop task
- Counts how many Stroop answers the user gets correct
- Displays final performance results
- Allows the user to play again without restarting the program

## File Structure
- `README.md` — project documentation
- `main.py` — main game code, GUI logic, helper functions, and game flow
- `tests/test_project.py` — unit tests for helper functions
- `requirements.txt` — lists packages needed for testing

## Approach
This project was designed using a modular approach. Each major part of the game is handled by a separate function or method.

The reaction-time portion uses randomized wait times and Python's timing tools to simulate a basic response-speed task. The memory portion generates a new random number sequence each time, checks the user's recall, and increases the sequence length after each correct answer. The Stroop portion randomly displays color words in mismatched colors and gives the user 30 seconds to answer as many as possible.

The GUI was built with Tkinter so that the program opens in a separate application window rather than relying only on terminal input. The design focused on creating a working cognitive task game first, then adding more rounds, adaptive difficulty, a timer, and final performance feedback.

## Main Functions
### `generate_sequence(length)`
Generates a random list of digit strings for the memory task.

### `calculate_average(values)`
Computes the average of a list of numbers.

### `check_memory_answer(user_answer, sequence)`
Checks whether the user's typed memory response matches the original sequence.

### `check_stroop_answer(user_answer, correct_color)`
Checks whether the user's typed answer matches the displayed text color.

### `main()`
Creates the Tkinter window and starts the game.

## How to Run
Make sure Python 3 is installed on your computer.

First, clone or download this repository. Then open a terminal in the project folder.

Run the program with:

```bash
python3 main.py
```

If your computer uses `python` instead of `python3`, run:

```bash
python main.py
```

A Tkinter window should open with the game instructions and a **Start Game** button.

## How to Play
1. Open the program.
2. Read the instructions on the opening screen.
3. Click **Start Game**.

### Round 1: Reaction Time
1. Wait for the **GO** signal.
2. Press the space bar as quickly as possible.
3. Complete all reaction-time rounds.
4. The program records your reaction times.

### Round 2: Memory Challenge
1. Memorize the number sequence shown on the screen.
2. After the sequence disappears, type it back with spaces between each number.
3. Each correct answer makes the next sequence one digit longer.
4. The memory round continues until you make a mistake.

Example answer format:

```text
1 4 8 2
```

### Round 3: Stroop Attention Task
1. A color word will appear on the screen.
2. Type the color of the text, not the word itself.
3. Try to get as many correct answers as possible in 30 seconds.

For example, if the word says `RED` but the text color is blue, you should type:

```text
blue
```

## Final Results
At the end of the game, the program displays:

- Average reaction time
- Best reaction time
- Memory score
- Longest sequence attempted
- Stroop score in 30 seconds

## How to Run Tests
This project includes unit tests in the `tests/` folder.

If needed, install pytest with:

```bash
pip install pytest
```

Then run the tests with:

```bash
pytest
```

The tests check the helper functions used in the project, including sequence generation, average calculation, memory answer checking, and Stroop answer checking.

## Requirements
This project uses Python's built-in modules:

- `tkinter`
- `random`
- `time`

The only extra package needed for testing is:

```text
pytest
```

## Notes
This project should run as-is after downloading the repository. If pytest is not installed, it is only needed for running the tests and not for playing the game.