import random
import time


def generate_sequence(length):
    """Generate a random sequence of digits for the memory test."""
    return [str(random.randint(0, 9)) for _ in range(length)]


def run_memory_test(length):
    """Run a memory test and return 1 if correct, otherwise 0."""
    sequence = generate_sequence(length)
    print("Memorize this sequence:")
    print(" ".join(sequence))
    time.sleep(3)
    print("\n" * 50)

    user_answer = input("Enter the sequence separated by spaces: ").split()

    if user_answer == sequence:
        print("Correct!")
        return 1

    print("Incorrect.")
    print("The correct sequence was:", " ".join(sequence))
    return 0


def run_reaction_test(rounds):
    """Run reaction time rounds and return a list of reaction times."""
    reaction_times = []

    for round_number in range(1, rounds + 1):
        print(f"Round {round_number}: Wait for GO!")
        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)

        print("GO!")
        start_time = time.time()
        input("Press Enter as fast as you can: ")
        end_time = time.time()

        reaction_time = end_time - start_time
        reaction_times.append(reaction_time)
        print(f"Your reaction time was {reaction_time:.3f} seconds.\n")

    return reaction_times


def summarize_results(reaction_times, memory_score):
    """Print a summary of the user's performance."""
    if reaction_times:
        average_time = sum(reaction_times) / len(reaction_times)
    else:
        average_time = 0

    print("\nFinal Results")
    print(f"Average reaction time: {average_time:.3f} seconds")
    print(f"Memory score: {memory_score}")


def main():
    """Run the reaction time and memory mini-game."""
    print("Welcome to the Reaction Time Memory Game!")

    reaction_times = run_reaction_test(3)
    memory_score = run_memory_test(5)
    summarize_results(reaction_times, memory_score)


if __name__ == "__main__":
    main()